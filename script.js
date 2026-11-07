/**
 * APEX IRON ATHLETIC CLUB - INTERACTIVE LOGIC & ANIMATIONS
 */

document.addEventListener('DOMContentLoaded', () => {
  initCustomCursor();
  initNavbarScroll();
  initMobileMenu();
  initCapacityPopover();
  initScrollReveal();
  initNumberCounters();
  initZoneSwitcher();
  initEquipmentFilters();
  initEquipmentModal();
  initPricingToggle();
  initFaqAccordion();
  initModals();
  initTourModal();
  initFormsAndButtons();
});

/* ==========================================================================
   1. CUSTOM CURSOR
   ========================================================================== */
function initCustomCursor() {
  const cursor = document.getElementById('customCursor');
  const follower = document.getElementById('cursorFollower');
  if (!cursor || !follower) return;

  let mouseX = 0, mouseY = 0;
  let followerX = 0, followerY = 0;

  window.addEventListener('mousemove', (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
    cursor.style.left = `${mouseX}px`;
    cursor.style.top = `${mouseY}px`;
  });

  function animateFollower() {
    followerX += (mouseX - followerX) * 0.15;
    followerY += (mouseY - followerY) * 0.15;
    follower.style.left = `${followerX}px`;
    follower.style.top = `${followerY}px`;
    requestAnimationFrame(animateFollower);
  }
  animateFollower();

  // Hover scale effect on interactive elements
  const interactives = document.querySelectorAll('a, button, input, select, .hotspot, .filter-pill, .equip-card, .live-badge');
  interactives.forEach(el => {
    el.addEventListener('mouseenter', () => {
      follower.style.transform = 'translate(-50%, -50%) scale(1.6)';
      follower.style.borderColor = 'rgba(255, 170, 0, 0.8)';
      cursor.style.transform = 'translate(-50%, -50%) scale(1.4)';
      cursor.style.backgroundColor = '#ffaa00';
    });
    el.addEventListener('mouseleave', () => {
      follower.style.transform = 'translate(-50%, -50%) scale(1)';
      follower.style.borderColor = 'rgba(0, 240, 255, 0.4)';
      cursor.style.transform = 'translate(-50%, -50%) scale(1)';
      cursor.style.backgroundColor = '#00f0ff';
    });
  });
}

/* ==========================================================================
   2. NAVBAR SCROLL EFFECT
   ========================================================================== */
function initNavbarScroll() {
  const navbarWrapper = document.querySelector('.navbar-wrapper');
  if (!navbarWrapper) return;

  const onScroll = () => {
    if (window.scrollY > 40) {
      navbarWrapper.classList.add('scrolled');
    } else {
      navbarWrapper.classList.remove('scrolled');
    }
  };

  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
}

/* ==========================================================================
   3. MOBILE NAVIGATION MENU
   ========================================================================== */
function initMobileMenu() {
  const toggle = document.getElementById('mobileToggle');
  const menu = document.getElementById('navMenu');
  const navLinks = document.querySelectorAll('.nav-link');

  if (!toggle || !menu) return;

  toggle.addEventListener('click', () => {
    menu.classList.toggle('open');
  });

  navLinks.forEach(link => {
    link.addEventListener('click', () => {
      menu.classList.remove('open');
    });
  });
}

/* ==========================================================================
   4. LIVE CAPACITY POPOVER
   ========================================================================== */
function initCapacityPopover() {
  const badge = document.getElementById('liveCapacityToggle');
  const popover = document.getElementById('capacityPopover');
  if (!badge || !popover) return;

  badge.addEventListener('click', (e) => {
    e.stopPropagation();
    popover.classList.toggle('show');
  });

  document.addEventListener('click', (e) => {
    if (!badge.contains(e.target)) {
      popover.classList.remove('show');
    }
  });
}

/* ==========================================================================
   5. SCROLL REVEAL (ROBUST VIEWPORT CHECK)
   ========================================================================== */
function initScrollReveal() {
  const revealElements = document.querySelectorAll('.reveal-elem');
  if (!revealElements.length) return;

  function checkReveal() {
    const triggerBottom = window.innerHeight * 0.92;
    revealElements.forEach(el => {
      const top = el.getBoundingClientRect().top;
      if (top < triggerBottom) {
        el.classList.add('active');
      }
    });
  }

  window.addEventListener('scroll', checkReveal, { passive: true });
  window.addEventListener('resize', checkReveal);
  
  // Initial triggers
  checkReveal();
  setTimeout(checkReveal, 100);
  setTimeout(checkReveal, 500);
}

/* ==========================================================================
   6. NUMBER COUNTER ANIMATION
   ========================================================================== */
function initNumberCounters() {
  const statNumbers = document.querySelectorAll('.stat-number');
  if (!statNumbers.length) return;

  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const el = entry.target;
        const target = parseInt(el.getAttribute('data-count'), 10);
        animateCounter(el, target);
        obs.unobserve(el);
      }
    });
  }, { threshold: 0.3 });

  statNumbers.forEach(stat => observer.observe(stat));

  function animateCounter(elem, target) {
    let start = 0;
    const duration = 1600;
    const startTime = performance.now();

    function update(now) {
      const elapsed = now - startTime;
      const progress = Math.min(elapsed / duration, 1);
      const easeProgress = 1 - Math.pow(1 - progress, 3);
      const current = Math.floor(easeProgress * target);

      elem.textContent = current.toLocaleString();

      if (progress < 1) {
        requestAnimationFrame(update);
      } else {
        elem.textContent = target.toLocaleString();
      }
    }
    requestAnimationFrame(update);
  }
}

/* ==========================================================================
   7. ZONE SWITCHER (INDOOR VS OUTDOOR DUAL REALMS)
   ========================================================================== */
function initZoneSwitcher() {
  const zoneBtns = document.querySelectorAll('.zone-btn');
  const facilityCards = document.querySelectorAll('.facility-card');

  if (!zoneBtns.length || !facilityCards.length) return;

  zoneBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      zoneBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const target = btn.getAttribute('data-target');

      facilityCards.forEach(card => {
        const category = card.getAttribute('data-category');
        if (target === 'all' || target === category) {
          card.classList.remove('hidden-zone');
          card.classList.add('active');
        } else {
          card.classList.add('hidden-zone');
        }
      });
    });
  });
}

/* ==========================================================================
   8. EQUIPMENT CATEGORY FILTERS
   ========================================================================== */
function initEquipmentFilters() {
  const filterPills = document.querySelectorAll('.filter-pill');
  const equipCards = document.querySelectorAll('.equip-card');

  if (!filterPills.length || !equipCards.length) return;

  filterPills.forEach(pill => {
    pill.addEventListener('click', () => {
      filterPills.forEach(p => p.classList.remove('active'));
      pill.classList.add('active');

      const filter = pill.getAttribute('data-filter');

      equipCards.forEach(card => {
        const category = card.getAttribute('data-category');
        if (filter === 'all' || filter === category) {
          card.style.display = 'flex';
          card.classList.add('active');
        } else {
          card.style.display = 'none';
        }
      });
    });
  });
}

/* ==========================================================================
   9. EQUIPMENT DETAILS MODAL & SPECS DATABASE
   ========================================================================== */
const equipmentDatabase = {
  hacksquat: {
    name: "Linear Hack Squat (45° Incline)",
    brand: "Arsenal Strength (USA)",
    category: "Heavy Strength & ISO",
    specs: [
      { label: "Frame Construction", val: "7-gauge 4x2 inch heavy-wall steel tubing" },
      { label: "Weight Horn Capacity", val: "1,200 lbs (600 kg) plate load capacity" },
      { label: "Footplate Dimensions", val: "30\" x 26\" Extra-wide diamond tread aluminum" },
      { label: "Linear Bearings", val: "Industrial linear recirculating ball bearings" },
      { label: "Target Muscle Groups", val: "Quadriceps (Vastus Medialis/Lateralis), Glutes" }
    ],
    features: "Equipped with dual lockout handles, adjustable safety stop increments every 2 inches, and dual band attachment pegs for ascending/descending resistance profiles."
  },
  eleiko: {
    name: "IPF Competition Power Bar & Calibrated Cast Plates",
    brand: "Eleiko (Sweden)",
    category: "Free Weights & Barbells",
    specs: [
      { label: "Steel Tensile Strength", val: "215,000 PSI Swedish proprietary steel" },
      { label: "Shaft Diameter", val: "29 mm precision aggressive pyramid knurling" },
      { label: "Plate Tolerance", val: "+/- 10 grams certified competition calibration" },
      { label: "Sleeve Rotation", val: "Precision bronze bushings with dust seals" },
      { label: "Target Disciplines", val: "Powerlifting, Squat, Bench Press, Deadlift" }
    ],
    features: "Used in world championship competitions worldwide. The chrome coating and 1.5mm sharp knurling provide unmatched grip friction under heavy load with zero bar deflection."
  },
  woodway: {
    name: "Curve Non-Motorized Slat-Belt Treadmill",
    brand: "Woodway (Germany)",
    category: "Smart Cardio & Slat",
    specs: [
      { label: "Drive Mechanism", val: "100% User kinetic propulsion (Zero electricity)" },
      { label: "Surface Type", val: "Individual vulcanized rubber slats (T-slat system)" },
      { label: "Caloric Burn Boost", val: "Burns up to 30% more energy than motorized treadmills" },
      { label: "Telemetry", val: "Live Wattage output, Split Pace, RPM, Heart Rate" },
      { label: "Target Goals", val: "Sprint acceleration, Aerobic capacity, Bio-stride" }
    ],
    features: "Curved running geometry absorbs high impact shock on knee and hip joints while enforcing a mid-foot natural running strike and instantaneous speed changes without button lag."
  },
  primechest: {
    name: "SmartStrength Seated Incline Chest Press",
    brand: "Prime Fitness (USA)",
    category: "Heavy Strength & ISO",
    specs: [
      { label: "Cam Technology", val: "Tri-Phase variable torque adjustment cam" },
      { label: "Arm Linkage", val: "Converging isolateral independent axis" },
      { label: "Seat Adjustment", val: "Pneumatic assisted height positioning" },
      { label: "Max Plate Capacity", val: "350 lbs per independent side" },
      { label: "Target Muscle Groups", val: "Clavicular Pectoralis Major, Anterior Deltoids" }
    ],
    features: "The patented SmartStrength cam allows the user to shift the peak resistance to the initial stretch position, the mid-range leverage, or the final peak contraction."
  },
  roguemonster: {
    name: "Custom Skyline Rooftop Calisthenics Rig",
    brand: "Rogue Fitness (Monster Series)",
    category: "Outdoor & Rigs",
    specs: [
      { label: "Uprights", val: "3x3\" 11-Gauge steel with laser-cut keyhole spacing" },
      { label: "Weather Treatment", val: "Multi-layer marine zinc primer & UV matte textured powder" },
      { label: "Attachments Included", val: "Gymnastics rings, salmon ladder, neutral grip bars" },
      { label: "Overall Footprint", val: "40 ft length x 14 ft depth x 12 ft height" },
      { label: "Target Modalities", val: "Calisthenics, Muscle-ups, Human Flags, Obstacle Course" }
    ],
    features: "Engineered specifically for high-wind rooftop environments with industrial grade fasteners, enabling athletes to combine bodyweight power with open skyline vistas."
  },
  cryo: {
    name: "-110°C Electric Whole-Body Cryotherapy Chamber",
    brand: "Cryo Science (Arctic Suite)",
    category: "Recovery & Cryo",
    specs: [
      { label: "Operating Temp", val: "-110°C (-166°F) True uniform ambient cold" },
      { label: "Cooling Tech", val: "100% Breathable electric refrigeration (No nitrogen gas)" },
      { label: "Session Duration", val: "2.5 to 3.5 minutes per protocol" },
      { label: "Safety Systems", val: "Dual infrared thermal mapping & pulse ox monitors" },
      { label: "Physiological Benefits", val: "Vascular vasoconstriction, endorphin surge, reduced DOMS" }
    ],
    features: "A medical-grade recovery device that triggers systemic cold shock proteins, drastically lowering systemic inflammation and accelerating muscular recovery between high-load workouts."
  }
};

function initEquipmentModal() {
  const modal = document.getElementById('equipDetailModal');
  const modalContent = document.getElementById('equipModalContent');
  const closeBtn = document.getElementById('closeEquipModalBtn');
  const detailButtons = document.querySelectorAll('.btn-equip-detail');

  if (!modal || !modalContent) return;

  detailButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const equipKey = btn.getAttribute('data-equip');
      const item = equipmentDatabase[equipKey];
      if (!item) return;

      let specsHtml = item.specs.map(s => `
        <div class="spec-detail-row" style="display:flex; justify-content:space-between; padding:0.65rem 0; border-bottom:1px solid var(--border-subtle); font-size:0.85rem;">
          <span style="color:var(--text-muted); font-family:var(--font-mono);">${s.label}</span>
          <span style="color:#ffffff; font-weight:600; text-align:right;">${s.val}</span>
        </div>
      `).join('');

      modalContent.innerHTML = `
        <div style="margin-bottom:1.5rem;">
          <div style="display:inline-block; font-family:var(--font-mono); font-size:0.75rem; color:var(--accent-gold); font-weight:700; margin-bottom:0.3rem;">
            ${item.brand}
          </div>
          <h3 style="font-size:1.6rem; color:#ffffff; margin-bottom:0.5rem;">${item.name}</h3>
          <p style="color:var(--text-muted); font-size:0.9rem; line-height:1.6; margin-bottom:1.5rem;">
            ${item.features}
          </p>
        </div>
        <div style="background:rgba(255,255,255,0.02); border:1px solid var(--border-subtle); border-radius:var(--radius-md); padding:1.25rem; margin-bottom:1.5rem;">
          <h4 style="font-size:0.95rem; font-family:var(--font-mono); color:var(--accent-cyan); margin-bottom:0.85rem; letter-spacing:0.1em;">
            <i class="fa-solid fa-microchip"></i> ENGINEERING SPECIFICATIONS
          </h4>
          ${specsHtml}
        </div>
        <button class="btn btn-primary btn-block" onclick="document.getElementById('equipDetailModal').classList.remove('active'); document.getElementById('passModal').classList.add('active');">
          <span>Test This Machine (Claim VIP Pass)</span>
          <i class="fa-solid fa-arrow-right"></i>
        </button>
      `;

      modal.classList.add('active');
    });
  });

  if (closeBtn) {
    closeBtn.addEventListener('click', () => modal.classList.remove('active'));
  }

  modal.addEventListener('click', (e) => {
    if (e.target === modal) modal.classList.remove('active');
  });
}

/* ==========================================================================
   10. PRICING TOGGLE (ANNUAL VS MONTHLY)
   ========================================================================== */
function initPricingToggle() {
  const toggle = document.getElementById('pricingToggle');
  const priceVals = document.querySelectorAll('.price-val');
  if (!toggle || !priceVals.length) return;

  toggle.addEventListener('change', () => {
    const isAnnual = toggle.checked;
    priceVals.forEach(val => {
      const monthly = val.getAttribute('data-monthly');
      const annual = val.getAttribute('data-annual');
      val.textContent = isAnnual ? annual : monthly;
    });
  });
}

/* ==========================================================================
   11. FAQ ACCORDION
   ========================================================================== */
function initFaqAccordion() {
  const faqItems = document.querySelectorAll('.faq-item');
  if (!faqItems.length) return;

  faqItems.forEach(item => {
    const question = item.querySelector('.faq-question');
    question.addEventListener('click', () => {
      const isActive = item.classList.contains('active');
      faqItems.forEach(i => i.classList.remove('active'));
      if (!isActive) {
        item.classList.add('active');
      }
    });
  });
}

/* ==========================================================================
   12. MODAL WINDOWS (VIP PASS & GUEST PASS)
   ========================================================================== */
function initModals() {
  const passModal = document.getElementById('passModal');
  const openPassBtns = [
    document.getElementById('openPassModalBtn'),
    document.getElementById('heroBookTourBtn'),
    document.getElementById('footerClaimPass'),
    ...document.querySelectorAll('.select-tier-btn')
  ].filter(Boolean);

  const closeModalBtn = document.getElementById('closeModalBtn');
  const passForm = document.getElementById('passForm');
  const modalSuccessState = document.getElementById('modalSuccessState');
  const closeSuccessBtn = document.getElementById('closeSuccessBtn');

  openPassBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      if (passModal) {
        passModal.classList.add('active');
        if (passForm && modalSuccessState) {
          passForm.style.display = 'block';
          modalSuccessState.style.display = 'none';
        }
      }
    });
  });

  if (closeModalBtn && passModal) {
    closeModalBtn.addEventListener('click', () => passModal.classList.remove('active'));
  }

  if (passModal) {
    passModal.addEventListener('click', (e) => {
      if (e.target === passModal) passModal.classList.remove('active');
    });
  }

  if (passForm && modalSuccessState) {
    passForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const submitBtn = passForm.querySelector('button[type="submit"]');
      if (submitBtn) {
        submitBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Confirming...';
      }

      setTimeout(() => {
        passForm.style.display = 'none';
        modalSuccessState.style.display = 'block';
        showToast("VIP Invitation Generated Successfully! Check your inbox.");
        if (submitBtn) {
          submitBtn.innerHTML = '<span>Confirm VIP Invitation</span> <i class="fa-solid fa-check"></i>';
        }
      }, 700);
    });
  }

  if (closeSuccessBtn && passModal) {
    closeSuccessBtn.addEventListener('click', () => passModal.classList.remove('active'));
  }
}

/* ==========================================================================
   13. 3D VIRTUAL TOUR MODAL & CONTROLS
   ========================================================================== */
function initTourModal() {
  const tourModal = document.getElementById('tourModal');
  const startTourBtn = document.getElementById('start3dTourBtn');
  const closeTourBtn = document.getElementById('closeTourModalBtn');
  const switchBtns = document.querySelectorAll('.tour-switch-btn');
  const indoorView = document.getElementById('tourIndoorView');
  const outdoorView = document.getElementById('tourOutdoorView');

  if (!tourModal) return;

  if (startTourBtn) {
    startTourBtn.addEventListener('click', () => {
      tourModal.classList.add('active');
    });
  }

  if (closeTourBtn) {
    closeTourBtn.addEventListener('click', () => {
      tourModal.classList.remove('active');
    });
  }

  tourModal.addEventListener('click', (e) => {
    if (e.target === tourModal) tourModal.classList.remove('active');
  });

  switchBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      switchBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const view = btn.getAttribute('data-view');
      if (view === 'indoor') {
        indoorView.classList.add('active-view');
        outdoorView.classList.remove('active-view');
      } else {
        outdoorView.classList.add('active-view');
        indoorView.classList.remove('active-view');
      }
    });
  });
}

/* ==========================================================================
   14. FORMS, TOASTS & INTERACTIONS
   ========================================================================== */
function initFormsAndButtons() {
  // Facility Gallery Buttons
  const galleryBtns = document.querySelectorAll('.facility-gallery-btn');
  galleryBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const type = btn.getAttribute('data-gallery');
      const equipSection = document.getElementById('equipment');
      if (equipSection) {
        equipSection.scrollIntoView({ behavior: 'smooth' });
        const filterPill = document.querySelector(`.filter-pill[data-filter="${type === 'indoor' ? 'strength' : 'calisthenics'}"]`);
        if (filterPill) filterPill.click();
      }
    });
  });

  // Coach booking buttons
  const coachBtns = document.querySelectorAll('.book-coach-btn');
  coachBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const coach = btn.getAttribute('data-coach');
      showToast(`Consultation request for ${coach} opened.`);
      const passModal = document.getElementById('passModal');
      if (passModal) passModal.classList.add('active');
    });
  });

  // Spec Sheet Download button
  const downloadBtn = document.getElementById('downloadSpecSheetBtn');
  if (downloadBtn) {
    downloadBtn.addEventListener('click', () => {
      downloadBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Preparing 2026 PDF...';
      setTimeout(() => {
        downloadBtn.innerHTML = '<i class="fa-solid fa-check"></i> Spec Sheet Downloaded';
        showToast("Apex Iron 2026 Hardware Spec Sheet PDF (240+ Units) downloaded.");
        setTimeout(() => {
          downloadBtn.innerHTML = '<i class="fa-solid fa-file-arrow-down"></i> <span>Download Full Equipment PDF</span>';
        }, 3000);
      }, 800);
    });
  }

  // Newsletter Form
  const newsletterForm = document.getElementById('newsletterForm');
  const newsletterStatus = document.getElementById('newsletterStatus');
  if (newsletterForm) {
    newsletterForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const emailInput = document.getElementById('newsletterEmail');
      if (emailInput && emailInput.value) {
        newsletterStatus.style.color = '#10b981';
        newsletterStatus.textContent = 'Subscribed to Performance Intel briefings.';
        emailInput.value = '';
        showToast("Subscribed to Apex Iron Performance Intel briefings.");
      }
    });
  }
}

function showToast(message) {
  const container = document.getElementById('toastContainer');
  if (!container) return;

  const toast = document.createElement('div');
  toast.className = 'toast';
  toast.innerHTML = `<i class="fa-solid fa-circle-info" style="color:var(--accent-cyan);"></i> <span>${message}</span>`;
  container.appendChild(toast);

  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transform = 'translateX(100%)';
    toast.style.transition = 'opacity 0.3s, transform 0.3s';
    setTimeout(() => toast.remove(), 300);
  }, 3500);
}
