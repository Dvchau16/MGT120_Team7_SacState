(function () {
  'use strict';

  const panels   = Array.from(document.querySelectorAll('.panel'));
  const dots     = Array.from(document.querySelectorAll('.dot'));
  const folio    = document.getElementById('stripCurrent');
  const TOTAL    = panels.length;
  const TL_IDX   = panels.findIndex(p => p.id === 'p12');

  let current        = 0;
  let busy           = false;
  let tlZoomed       = false;

  // ── Navigate to panel ─────────────────────────────────────────────────────
  function goTo(idx) {
    if (idx < 0 || idx >= TOTAL || idx === current || busy) return;
    busy = true;

    panels[current].classList.remove('active');
    dots[current].classList.remove('active');

    current = idx;

    panels[current].classList.add('active');
    dots[current].classList.add('active');

    if (folio) folio.textContent = String(current + 1).padStart(2, '0');

    setTimeout(() => { busy = false; }, 900);
  }

  function next() {
    if (current === TL_IDX && !tlZoomed) { triggerZoomOut(); return; }
    goTo(current + 1);
  }

  function prev() { goTo(current - 1); }

  // ── Timeline two-state ────────────────────────────────────────────────────
  // Default: Phase 0 hero (large text, no distortion)
  // After spacebar/button: full 4-year view fades in
  const tlZoomBtn = document.getElementById('tlZoomBtn');
  const tlPhase0  = document.getElementById('tlPhase0');
  const tlFull    = document.getElementById('tlFull');

  function triggerZoomOut() {
    if (tlZoomed) return;
    tlZoomed = true;
    if (tlPhase0) tlPhase0.classList.add('hidden');
    if (tlFull) {
      tlFull.style.display = 'block';
      requestAnimationFrame(() => requestAnimationFrame(() => tlFull.classList.add('visible')));
    }
    if (tlZoomBtn) tlZoomBtn.textContent = '← Back to Phase 0';
  }

  function triggerZoomIn() {
    tlZoomed = false;
    if (tlPhase0) tlPhase0.classList.remove('hidden');
    if (tlFull) {
      tlFull.classList.remove('visible');
      setTimeout(() => { tlFull.style.display = 'none'; }, 600);
    }
    if (tlZoomBtn) tlZoomBtn.textContent = 'See all four years →';
  }

  if (tlZoomBtn) {
    tlZoomBtn.addEventListener('click', e => {
      e.stopPropagation();
      tlZoomed ? triggerZoomIn() : triggerZoomOut();
    });
  }

  // ── Build timeline from injected data ─────────────────────────────────────
  function buildHalf(rangeStart, rangeEnd, evId, phId) {
    const evC = document.getElementById(evId);
    const phC = document.getElementById(phId);
    if (!evC || !phC) return;

    const scale = 100 / (rangeEnd - rangeStart);

    (window.TIMELINE_EVENTS || []).forEach(ev => {
      if (ev.position < rangeStart || ev.position >= rangeEnd) return;
      const pos = (ev.position - rangeStart) * scale;
      const el = document.createElement('div');
      el.className = 'tl-event';
      el.style.left = pos + '%';
      el.innerHTML = `
        <div class="tl-event__dot" style="background:${ev.color};"></div>
        <div class="tl-event__label">${ev.label}</div>`;
      evC.appendChild(el);
    });

    const visiblePhases = (window.PHASES || [])
      .map(ph => ({ ...ph, pStart: Math.max(ph.start, rangeStart), pEnd: Math.min(ph.end, rangeEnd) }))
      .filter(ph => ph.pStart < ph.pEnd);

    if (visiblePhases.length) visiblePhases[visiblePhases.length - 1].pEnd = rangeEnd;

    visiblePhases.forEach(({ pStart, pEnd, color, label, stat }) => {
      const el = document.createElement('div');
      el.className = 'tl-phase';
      el.style.left       = ((pStart - rangeStart) * scale) + '%';
      el.style.width      = ((pEnd - pStart) * scale) + '%';
      el.style.background = color;
      el.innerHTML = `
        <div class="tl-phase__label">${label}</div>
        <div class="tl-phase__stat">${stat}</div>`;
      phC.appendChild(el);
    });
  }

  function buildTimeline() {
    buildHalf(0,  50, 'tlEvents',  'tlPhases');   // 2026–2028
    buildHalf(50, 100, 'tlEvents2', 'tlPhases2'); // 2028–2030
  }

  buildTimeline();

  // ── Keyboard ───────────────────────────────────────────────────────────────
  document.addEventListener('keydown', e => {
    switch (e.key) {
      case ' ':
      case 'ArrowDown':
      case 'ArrowRight':
        e.preventDefault(); next(); break;
      case 'ArrowUp':
      case 'ArrowLeft':
        e.preventDefault(); prev(); break;
    }
  });

  // ── Mouse wheel (700ms debounce) ───────────────────────────────────────────
  let wLast = 0;
  window.addEventListener('wheel', e => {
    e.preventDefault();
    const now = Date.now();
    if (now - wLast < 700) return;
    wLast = now;
    e.deltaY > 0 ? next() : prev();
  }, { passive: false });

  // ── Touch swipe ────────────────────────────────────────────────────────────
  let tY = null;
  document.addEventListener('touchstart', e => { tY = e.touches[0].clientY; }, { passive: true });
  document.addEventListener('touchend', e => {
    if (tY === null) return;
    const dy = tY - e.changedTouches[0].clientY;
    if (Math.abs(dy) > 40) { dy > 0 ? next() : prev(); }
    tY = null;
  }, { passive: true });

  // ── Dot clicks ─────────────────────────────────────────────────────────────
  dots.forEach((dot, i) => dot.addEventListener('click', () => goTo(i)));

  // ── Init ───────────────────────────────────────────────────────────────────
  goTo(0);

})();
