/* CARER — main.js
   Scroll-reveal + nav scroll-shadow + mobile menu */
(function () {
  'use strict';

  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* --- Scroll reveal ----------------------------------------- */
  const revealEls = document.querySelectorAll('[data-reveal]');
  if (!reduce && 'IntersectionObserver' in window && revealEls.length) {
    revealEls.forEach(el => {
      el.style.opacity = '0';
      el.style.transform = 'translateY(26px)';
      el.style.transition = 'opacity 0.9s ease, transform 0.9s ease';
    });
    const io = new IntersectionObserver(entries => {
      entries.forEach(en => {
        if (en.isIntersecting) {
          en.target.style.opacity = '1';
          en.target.style.transform = 'translateY(0)';
          io.unobserve(en.target);
        }
      });
    }, { threshold: 0.10 });
    revealEls.forEach(el => io.observe(el));
  }

  /* --- Nav scroll-shadow ------------------------------------- */
  const nav = document.querySelector('.site-nav');
  if (nav) {
    const onScroll = () => {
      nav.style.boxShadow = window.scrollY > 10
        ? '0 2px 20px rgba(168,102,60,0.10)'
        : '';
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  /* --- Mobile hamburger toggle ------------------------------- */
  const hamburger = document.querySelector('.nav-hamburger');
  const navLinks  = document.querySelector('.nav-links');
  if (hamburger && navLinks) {
    hamburger.addEventListener('click', () => {
      const open = navLinks.classList.toggle('open');
      hamburger.setAttribute('aria-expanded', String(open));
      hamburger.textContent = open ? '✕' : '☰';
    });
    // Close on nav link click
    navLinks.querySelectorAll('a').forEach(a => {
      a.addEventListener('click', () => {
        navLinks.classList.remove('open');
        hamburger.setAttribute('aria-expanded', 'false');
        hamburger.textContent = '☰';
      });
    });
  }
})();
