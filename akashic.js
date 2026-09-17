(function () {
  var root = document.documentElement;
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var nav = document.querySelector('.nav');
  if (nav) {
    var onNav = function () { nav.classList.toggle('scrolled', (window.scrollY || 0) > 12); };
    window.addEventListener('scroll', onNav, { passive: true });
    onNav();
  }
  if (root.classList.contains('js-reveal')) {
    var groups = ['.stats-grid', '.compare-grid', '.feat-grid', '.demo-grid', '.tools-grid', '.price-grid', '.caveat-list', '.faq-list', '.pipe-track'];
    groups.forEach(function (sel) {
      document.querySelectorAll(sel).forEach(function (grid) {
        var i = 0;
        Array.prototype.forEach.call(grid.children, function (c) {
          if (c.nodeType === 1) { c.classList.add('reveal'); c.style.setProperty('--reveal-i', i % 5); i++; }
        });
      });
    });
    document.querySelectorAll('.sec-head, .brokers, .price-promo, .final-cta-card, .offer-plate, .about-copy, .support-form, .support-side, .pipe-latency')
      .forEach(function (el) { el.classList.add('reveal'); });

    var revealEls = document.querySelectorAll('.reveal');
    if (!reduce && 'IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting) { e.target.classList.add('is-visible'); io.unobserve(e.target); }
        });
      }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });
      revealEls.forEach(function (el) { io.observe(el); });
    } else {
      revealEls.forEach(function (el) { el.classList.add('is-visible'); });
    }
  }
  var sectionLinks = Array.prototype.filter.call(
    document.querySelectorAll('.nav-links a[href*="#"]'),
    function (a) { return a.getAttribute('href').indexOf('#') >= 0; }
  );
  var idToLink = {};
  sectionLinks.forEach(function (a) {
    var hash = a.getAttribute('href').split('#')[1];
    if (hash) idToLink[hash] = a;
  });
  var watched = Object.keys(idToLink).map(function (id) { return document.getElementById(id); }).filter(Boolean);
  if (watched.length && 'IntersectionObserver' in window) {
    var navIo = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          sectionLinks.forEach(function (a) { a.classList.remove('is-active'); });
          var link = idToLink[e.target.id];
          if (link) link.classList.add('is-active');
        }
      });
    }, { rootMargin: '-45% 0px -50% 0px' });
    watched.forEach(function (s) { navIo.observe(s); });
  }
  if (!reduce && window.matchMedia('(pointer: fine)').matches) {
    document.querySelectorAll('.feat').forEach(function (card) {
      card.addEventListener('pointermove', function (e) {
        var r = card.getBoundingClientRect();
        card.style.setProperty('--mx', ((e.clientX - r.left) / r.width * 100) + '%');
        card.style.setProperty('--my', ((e.clientY - r.top) / r.height * 100) + '%');
      });
    });
  }

})();

(function () {
  var ring = document.getElementById('ring'); if (!ring) return;
  var wrap = document.getElementById('ring-wrap'), cap = document.getElementById('ring-cap');
  var cards = [].slice.call(ring.children), N = cards.length, step = 360 / N, i = 0, R = 0, timer, x0 = null;
  function place() {
    ring.style.transform = 'translateZ(' + (-R) + 'px) rotateY(' + (-i * step) + 'deg)';
    cards.forEach(function (c, k) {
      var a = k - i; a = a - Math.round(a / N) * N;
      var deg = Math.abs(a) * step;
      c.style.opacity = deg > 100 ? 0 : (1 - deg / 180 * 1.15).toFixed(2);
      c.classList.toggle('is-front', Math.abs(a) < 0.5);
    });
    cap.textContent = '#post-profits · ' + (((Math.round(i) % N) + N) % N + 1) + ' / ' + N;
  }
  function layout() {
    R = Math.round(cards[0].offsetWidth / 2 / Math.tan(Math.PI / N) * 1.06);
    ring.parentNode.style.height = (Math.max.apply(null, cards.map(function (c) { return c.offsetHeight; })) + 28) + 'px';
    cards.forEach(function (c, k) { c.style.transform = 'rotateY(' + (k * step) + 'deg) translateZ(' + R + 'px) translateY(-50%)'; });
    place();
  }
  function go(d) { i = (d > 0 ? Math.floor(i) : Math.ceil(i)) + d; place(); }
  function restart() { clearInterval(timer); if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) timer = setInterval(function () { go(1); }, 3200); }
  wrap.querySelector('.prev').addEventListener('click', function () { go(-1); restart(); });
  wrap.querySelector('.next').addEventListener('click', function () { go(1); restart(); });
  wrap.addEventListener('mouseenter', function () { clearInterval(timer); });
  wrap.addEventListener('mouseleave', restart);
  var acc = 0, lock = 0;
  wrap.addEventListener('wheel', function (e) {
    var over = cards.some(function (c) { if (!(+c.style.opacity)) return false; var r = c.getBoundingClientRect(); return e.clientX >= r.left && e.clientX <= r.right && e.clientY >= r.top && e.clientY <= r.bottom; });
    if (!over) return;
    e.preventDefault();
    var now = Date.now(); if (now < lock) return;
    acc += Math.abs(e.deltaY) >= Math.abs(e.deltaX) ? e.deltaY : e.deltaX;
    if (Math.abs(acc) > 24) { go(acc > 0 ? 1 : -1); acc = 0; lock = now + 500; restart(); }
  }, { passive: false });
  var dx = 0;
  wrap.addEventListener('pointerdown', function (e) {
    if (e.target.closest('.ring-nav') || e.button) return;
    x0 = e.clientX; dx = 0; clearInterval(timer); ring.classList.add('is-drag'); wrap.setPointerCapture(e.pointerId);
  });
  wrap.addEventListener('pointermove', function (e) {
    if (x0 === null) return;
    dx = e.clientX - x0;
    ring.style.transform = 'translateZ(' + (-R) + 'px) rotateY(' + (-i * step + dx / cards[0].offsetWidth * step) + 'deg)';
  });
  function release() {
    if (x0 === null) return;
    ring.classList.remove('is-drag');
    i -= dx / cards[0].offsetWidth; x0 = null; place(); restart();
  }
  wrap.addEventListener('pointerup', release); wrap.addEventListener('pointercancel', release);
  if ('IntersectionObserver' in window && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    var seen = false, io = new IntersectionObserver(function (es) {
      if (seen || !es[0].isIntersecting) return; seen = true; io.disconnect();
      ring.classList.add('is-whirl'); i += N; place();
      setTimeout(function () { ring.classList.remove('is-whirl'); }, 2500);
    }, { threshold: 0.35 });
    io.observe(ring.parentNode);
  }
  window.addEventListener('resize', layout); window.addEventListener('load', layout);
  layout(); restart();
})();

(function () {
  var form = document.querySelector('.signup');
  if (!form || !window.fetch) return;
  var status = form.querySelector('.signup-status'), btn = form.querySelector('button');
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    btn.disabled = true; status.className = 'signup-status'; status.textContent = 'Saving your seat…';
    fetch(form.action, { method: 'POST', body: new FormData(form), headers: { accept: 'application/json' } })
      .then(function (r) { return r.json(); })
      .then(function (d) {
        if (!d.ok) throw d.error;
        status.className = 'signup-status ok'; status.textContent = 'Seat saved. Watch your inbox for the invite.'; form.reset();
      })
      .catch(function (err) { status.className = 'signup-status err'; status.textContent = typeof err === 'string' ? err : 'That did not go through. Try again, or ask in the Discord.'; })
      .then(function () { btn.disabled = false; });
  });
})();
