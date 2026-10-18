/* muse-webcrawl shared browser helpers (dependency-free vanilla JS).
 *
 * Main job: fixImages(rootEl) — the no-service-worker fallback for the
 * base64 image bridge. Images in this repo are published as text files at
 * "<image-path>.b64" (the push channel is text-only) while pages reference
 * the plain image path. The service worker (sw.js) normally bridges that
 * gap; where no worker is active (first load, unsupported browser, worker
 * disabled), fixImages fetches each <img>'s ".b64" sibling, decodes it and
 * swaps in a blob: URL.
 *
 * Loaded by the landing UI (index.html); also exported as window.MuseWeb
 * for potential future use by other scaffolding pages.
 */
(function (global) {
  'use strict';

  var MIME_BY_EXT = {
    png: 'image/png',
    jpg: 'image/jpeg',
    jpeg: 'image/jpeg',
    webp: 'image/webp',
    gif: 'image/gif'
  };

  function mimeFor(url) {
    var m = /\.([a-z0-9]+)(?:[?#].*)?$/i.exec(url || '');
    if (!m) return 'application/octet-stream';
    return MIME_BY_EXT[m[1].toLowerCase()] || 'application/octet-stream';
  }

  /* Chunked atob decode — same algorithm as sw.js. */
  function b64ToBytes(b64) {
    var clean = String(b64).replace(/\s+/g, '');
    var CHUNK = 0x8000;
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

  function serviceWorkerActive() {
    return !!(
      global.navigator &&
      'serviceWorker' in global.navigator &&
      global.navigator.serviceWorker.controller
    );
  }

  /* Swap one <img> to a decoded blob URL. Returns a promise. */
  function fixImage(img) {
    if (!img || img.dataset.musewebFixed) return Promise.resolve(false);
    var src = img.getAttribute('src');
    if (!src || /^(data:|blob:)/i.test(src)) return Promise.resolve(false);
    img.dataset.musewebFixed = 'pending';

    var abs = img.src; // resolved absolute URL of the (missing) image
    return fetch(abs + '.b64', { credentials: 'same-origin' })
      .then(function (resp) {
        if (!resp.ok) throw new Error('b64 fetch ' + resp.status);
        return resp.text();
      })
      .then(function (text) {
        var bytes = b64ToBytes(text);
        if (!bytes.length) throw new Error('empty b64');
        var blob = new Blob([bytes], { type: mimeFor(abs) });
        img.src = URL.createObjectURL(blob);
        img.dataset.musewebFixed = 'done';
        return true;
      })
      .catch(function () {
        /* Leave the original src (and any alt text) in place. */
        delete img.dataset.musewebFixed;
        return false;
      });
  }

  /* Fix all images under rootEl (default: document). Skips work entirely
   * when a service worker already controls the page — the worker serves
   * decoded bytes at the original URL, so blob swapping is unnecessary. */
  function fixImages(rootEl) {
    if (serviceWorkerActive()) return Promise.resolve(0);
    var root = rootEl || document;
    var imgs = Array.prototype.slice.call(root.querySelectorAll('img'));
    return Promise.all(imgs.map(fixImage)).then(function (results) {
      return results.filter(Boolean).length;
    });
  }

  global.MuseWeb = {
    fixImages: fixImages,
    fixImage: fixImage,
    b64ToBytes: b64ToBytes,
    mimeFor: mimeFor,
    serviceWorkerActive: serviceWorkerActive
  };
})(typeof window !== 'undefined' ? window : this);
