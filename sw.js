/* muse-webcrawl image bridge service worker.
 *
 * Why this exists: the GitHub push channel for this repo is text-only, so
 * images are committed as base64 text files next to where the image would
 * live:  web/<domain>/<path>/images/foo.png.b64
 * The recreated HTML pages reference the plain path (images/foo.png), which
 * 404s on GitHub Pages. This worker intercepts those image requests, fetches
 * the sibling ".b64" file instead, decodes it in-browser, and serves the
 * real bytes with the right Content-Type. Decoded images are cached in
 * Cache Storage so repeat visits are fast.
 *
 * Scope: registered from index.html with scope './' (the repo root), so it
 * controls every page under the GitHub Pages site.
 */

'use strict';

var CACHE_NAME = 'museweb-img-v1';
var CACHE_PREFIX = 'museweb-img-';

var MIME_BY_EXT = {
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.webp': 'image/webp',
  '.gif': 'image/gif'
};

/* 1x1 transparent PNG, served when no .b64 sibling exists so pages show a
 * blank instead of a broken-image icon. */
var PIXEL_B64 =
  'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII=';

function b64ToBytes(b64) {
  /* Chunked atob so multi-megabyte images do not blow the argument/stack
   * limits. Chunk size is a multiple of 4 (base64 quantum). */
  var clean = String(b64).replace(/\s+/g, '');
  var CHUNK = 0x8000; // 32768 chars -> 24576 bytes per chunk
  var parts = [];
  var total = 0;
  for (var i = 0; i < clean.length; i += CHUNK) {
    var bin = atob(clean.slice(i, i + CHUNK));
    var bytes = new Uint8Array(bin.length);
    for (var j = 0; j < bin.length; j++) bytes[j] = bin.charCodeAt(j);
    parts.push(bytes);
    total += bytes.length;
  }
  var out = new Uint8Array(total);
  var off = 0;
  for (var k = 0; k < parts.length; k++) {
    out.set(parts[k], off);
    off += parts[k].length;
  }
  return out;
}

function pixelResponse() {
  return new Response(b64ToBytes(PIXEL_B64), {
    status: 200,
    headers: { 'Content-Type': 'image/png', 'Cache-Control': 'max-age=3600' }
  });
}

function imageExtension(pathname) {
  var lower = pathname.toLowerCase();
  var exts = Object.keys(MIME_BY_EXT);
  for (var i = 0; i < exts.length; i++) {
    if (lower.endsWith(exts[i])) return exts[i];
  }
  return null;
}

self.addEventListener('install', function (event) {
  /* Take over as soon as possible: a landing-page visit should make the
   * rest of the session's browsing controlled without a manual reload. */
  self.skipWaiting();
});

self.addEventListener('activate', function (event) {
  event.waitUntil(
    caches.keys().then(function (keys) {
      return Promise.all(
        keys.map(function (key) {
          if (key.indexOf(CACHE_PREFIX) === 0 && key !== CACHE_NAME) {
            return caches.delete(key);
          }
          return Promise.resolve(false);
        })
      );
    }).then(function () {
      return self.clients.claim();
    })
  );
});

self.addEventListener('fetch', function (event) {
  var request = event.request;

  /* Only plain GETs; let everything else go to the network untouched. */
  if (request.method !== 'GET') return;

  /* Never intercept navigations or documents/assets: only images. */
  if (request.mode === 'navigate') return;

  var url;
  try {
    url = new URL(request.url);
  } catch (e) {
    return;
  }

  /* Same-origin only: hotlinked images on other hosts are not ours. */
  if (url.origin !== self.location.origin) return;

  var pathname = url.pathname;

  /* Never intercept the .b64 files themselves or non-image assets. */
  if (pathname.toLowerCase().endsWith('.b64')) return;
  var ext = imageExtension(pathname);
  if (!ext) return; // covers .html/.json/.js/.css and everything else

  event.respondWith(serveDecodedImage(request, url, ext));
});

function serveDecodedImage(request, url, ext) {
  return caches.open(CACHE_NAME).then(function (cache) {
    return cache.match(request.url).then(function (cached) {
      if (cached) return cached;

      var b64url = url.toString() + '.b64';
      return fetch(b64url, { credentials: 'same-origin' })
        .then(function (resp) {
          if (!resp.ok) return pixelResponse();
          return resp.text().then(function (text) {
            var bytes;
            try {
              bytes = b64ToBytes(text);
            } catch (e) {
              return pixelResponse();
            }
            if (!bytes || bytes.length === 0) return pixelResponse();
            var response = new Response(bytes, {
              status: 200,
              headers: {
                'Content-Type': MIME_BY_EXT[ext],
                'Content-Length': String(bytes.length),
                'Cache-Control': 'public, max-age=31536000, immutable'
              }
            });
            /* Cache the decoded bytes under the original image URL. */
            cache.put(request.url, response.clone());
            return response;
          });
        })
        .catch(function () {
          return pixelResponse();
        });
    });
  });
}
