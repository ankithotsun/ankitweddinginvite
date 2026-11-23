# JavaScript for Ankit & Sharwani Wedding Invitation

JS = '''
// 0. Scroll Restoration: Never retain scroll position on refresh or open; strictly start from top
if ('scrollRestoration' in history) {
  history.scrollRestoration = 'manual';
}
window.scrollTo(0, 0);
if (document.documentElement) document.documentElement.scrollTop = 0;
if (document.body) document.body.scrollTop = 0;

window.addEventListener('pageshow', () => {
  window.scrollTo(0, 0);
  if (document.documentElement) document.documentElement.scrollTop = 0;
  if (document.body) document.body.scrollTop = 0;
});

window.addEventListener('beforeunload', () => {
  window.scrollTo(0, 0);
});

document.addEventListener('DOMContentLoaded', () => {
  window.scrollTo(0, 0);
  if (document.documentElement) document.documentElement.scrollTop = 0;
  if (document.body) document.body.scrollTop = 0;

  // =========================================================================
  // 1. Audio Setup with Resilient Mobile Autoplay & Gesture Unlocker
  // =========================================================================
  const bgAudio = document.getElementById('bg-audio');
  const audioController = document.getElementById('audio-controller');
  const vinylDisc = document.querySelector('.vinyl-disc');
  let isPlaying = false;
  let userManuallyMuted = false;

  function playMusic() {
    if (!bgAudio || userManuallyMuted) return;
    try {
      bgAudio.volume = 0.55;
    } catch(e) {}

    const playPromise = bgAudio.play();
    if (playPromise !== undefined) {
      playPromise.then(() => {
        isPlaying = true;
        if (vinylDisc) vinylDisc.classList.add('spinning');
        if (audioController) audioController.classList.add('audio-playing');
      }).catch(err => {
        // Autoplay deferred until user touch / scroll
      });
    }
  }

  function pauseMusic() {
    if (!bgAudio) return;
    bgAudio.pause();
    isPlaying = false;
    if (vinylDisc) vinylDisc.classList.remove('spinning');
    if (audioController) audioController.classList.remove('audio-playing');
  }

  function toggleAudio() {
    if (isPlaying) {
      userManuallyMuted = true;
      pauseMusic();
    } else {
      userManuallyMuted = false;
      playMusic();
    }
  }

  if (audioController) {
    audioController.addEventListener('click', (e) => {
      e.stopPropagation();
      toggleAudio();
    });
  }

  // Ensure music is auto-on once past the very first screen (either auto-scroll or manual)
  function ensureMusicPlaying() {
    if (userManuallyMuted) return;
    if (openingState !== 'CLOSED') {
      if (!isPlaying || (bgAudio && bgAudio.paused)) {
        playMusic();
      }
    }
  }

  const audioUnlockEvents = ['touchstart', 'touchend', 'click', 'pointerdown', 'scroll', 'touchmove', 'wheel'];
  audioUnlockEvents.forEach(evt => {
    window.addEventListener(evt, ensureMusicPlaying, { passive: true });
    document.addEventListener(evt, ensureMusicPlaying, { passive: true });
  });

  // =========================================================================
  // 2. Preloader & 3D Book Opening (Two-Stage Responsive Tap)
  // =========================================================================
  const openingStage = document.getElementById('opening-stage');
  const bookCover = document.getElementById('book-front-cover');
  const bookWrapper = document.getElementById('book-wrapper');
  const openInviteBtn = document.getElementById('open-invite-btn');
  const loaderContainer = document.getElementById('loader-container');
  const tapPrompt = document.getElementById('tap-to-open-prompt');

  // Stages: 'CLOSED' -> 'INSIDE_PAGE' -> 'MAIN_PAGE'
  let openingState = 'CLOSED';
  let autoOpenTimer = null;
  let autoEnterTimer = null;
  let lastOpeningTapTime = 0;
  let autoScrollAllowedAt = 0;

  setTimeout(() => {
    if (loaderContainer) loaderContainer.style.display = 'none';
    if (tapPrompt) tapPrompt.style.display = 'flex';
    
    // Auto-open book in 6s if guest does not tap
    autoOpenTimer = setTimeout(() => {
      if (openingState === 'CLOSED') {
        openBook();
      }
    }, 6000);
  }, 1200);

  function openBook() {
    if (openingState !== 'CLOSED') return;
    openingState = 'INSIDE_PAGE';
    if (autoOpenTimer) clearTimeout(autoOpenTimer);

    playMusic();

    if (bookCover) bookCover.classList.add('open-book');
    fireConfettiBurst();

    // Update button text on second screen so guest knows tapping enters the invitation immediately!
    if (openInviteBtn) {
      openInviteBtn.innerHTML = '<span>✨ Enter Invitation ✨</span>';
    }

    // Auto-enter in 5.5 seconds if guest does not tap second screen
    autoEnterTimer = setTimeout(() => {
      enterInvitation();
    }, 5500);
  }

  function enterInvitation() {
    if (openingState === 'MAIN_PAGE') return;
    openingState = 'MAIN_PAGE';
    autoScrollAllowedAt = Date.now() + 800; // 800ms grace period so opening tap does not turn off auto-scroll
    if (autoEnterTimer) clearTimeout(autoEnterTimer);

    playMusic();

    if (openingStage) {
      openingStage.classList.add('opened');
      setTimeout(() => {
        openingStage.style.display = 'none';
      }, 1900);
    }
    isAutoModeActive = true;
    currentSectionId = 'hero-section';
    prevVisibleSection = 'hero-section';

    window.scrollTo({ top: 0, left: 0, behavior: 'instant' });
    if (document.documentElement) document.documentElement.scrollTop = 0;
    if (document.body) document.body.scrollTop = 0;

    setTimeout(() => {
      startTypewriterAnimation();
    }, 400);
  }

  // Handle taps on book, button, or anywhere on the opening stage at either stage
  function handleOpeningTap(e) {
    const now = Date.now();
    if (now - lastOpeningTapTime < 350) return; // Prevent double fires from same touch gesture

    playMusic();

    if (openingState === 'CLOSED') {
      lastOpeningTapTime = now;
      openBook();
    } else if (openingState === 'INSIDE_PAGE') {
      // Tap on second screen IMMEDIATELY enters invitation on the very first tap!
      lastOpeningTapTime = now;
      enterInvitation();
    }
  }

  if (openingStage) {
    openingStage.addEventListener('click', handleOpeningTap);
    openingStage.addEventListener('touchend', handleOpeningTap, { passive: true });
  }

  if (bookWrapper) {
    bookWrapper.addEventListener('click', handleOpeningTap);
    bookWrapper.addEventListener('touchend', handleOpeningTap, { passive: true });
  }

  if (openInviteBtn) {
    openInviteBtn.addEventListener('click', handleOpeningTap);
    openInviteBtn.addEventListener('touchend', handleOpeningTap, { passive: true });
  }

  // =========================================================================
  // 3. Reliable Auto-Tour Engine & Clean Manual Scroll Handler
  // =========================================================================
  const sectionList = [
    { id: 'hero-section', getEl: () => document.getElementById('hero-section') },
    { id: 'save-the-date-section', getEl: () => document.getElementById('save-the-date-section') },
    { id: 'festivities-section', getEl: () => document.getElementById('festivities-section') },
    { id: 'story-section', getEl: () => document.getElementById('story-section') },
    { id: 'reception-section', getEl: () => document.getElementById('reception-section') },
    { id: 'location-section', getEl: () => document.getElementById('location-section') },
    { id: 'closing-section', getEl: () => document.querySelector('.closing-section') }
  ];

  function getVisibleSectionId() {
    const midY = window.innerHeight * 0.45;
    for (const sec of sectionList) {
      const el = sec.getEl();
      if (!el) continue;
      const rect = el.getBoundingClientRect();
      if (rect.top <= midY && rect.bottom >= midY) {
        return sec.id;
      }
    }

    let bestSec = 'hero-section';
    let maxVisibleH = -1;
    for (const sec of sectionList) {
      const el = sec.getEl();
      if (!el) continue;
      const rect = el.getBoundingClientRect();
      const visibleH = Math.max(0, Math.min(rect.bottom, window.innerHeight) - Math.max(rect.top, 0));
      if (visibleH > maxVisibleH) {
        maxVisibleH = visibleH;
        bestSec = sec.id;
      }
    }
    return bestSec;
  }

  let isAutoModeActive = true;
  let isProgrammaticScrolling = false;
  let currentSectionId = 'hero-section';
  let prevVisibleSection = 'opening-stage';

  let cardStepTimer = null;
  let sectionAdvanceTimer = null;

  function clearAllAutoTimers() {
    if (cardStepTimer) { clearTimeout(cardStepTimer); cardStepTimer = null; }
    if (sectionAdvanceTimer) { clearTimeout(sectionAdvanceTimer); sectionAdvanceTimer = null; }
  }

  // Requirement 4: If user taps or touches, auto-scroll is turned OFF immediately!
  function turnOffAutoScroll() {
    if (openingState !== 'MAIN_PAGE') return;
    if (Date.now() < autoScrollAllowedAt) return; // Prevent book opening tap from cancelling auto-scroll
    if (!isAutoModeActive) return;
    isAutoModeActive = false;
    clearAllAutoTimers();
  }

  window.addEventListener('touchstart', () => {
    if (openingState === 'MAIN_PAGE') {
      turnOffAutoScroll();
    }
  }, { passive: true });

  window.addEventListener('touchmove', () => {
    if (openingState === 'MAIN_PAGE') {
      turnOffAutoScroll();
    }
  }, { passive: true });

  window.addEventListener('pointerdown', () => {
    if (openingState === 'MAIN_PAGE') {
      turnOffAutoScroll();
    }
  }, { passive: true });

  window.addEventListener('wheel', () => {
    if (openingState === 'MAIN_PAGE') {
      turnOffAutoScroll();
    }
  }, { passive: true });

  window.addEventListener('click', () => {
    if (openingState === 'MAIN_PAGE') {
      turnOffAutoScroll();
    }
  }, { passive: true });

  // Resilient smooth scroll helper
  function scrollToSection(targetId, onCompleteCallback) {
    ensureMusicPlaying();
    const el = targetId === 'closing-section' ? 
               document.querySelector('.closing-section') : 
               document.getElementById(targetId);
    if (!el) return;

    isProgrammaticScrolling = true;
    currentSectionId = targetId;
    prevVisibleSection = targetId;

    el.scrollIntoView({ behavior: 'smooth', block: 'start' });

    setTimeout(() => {
      isProgrammaticScrolling = false;
      currentSectionId = targetId;
      prevVisibleSection = targetId;

      if (targetId === 'festivities-section') {
        currentFestIdx = 0;
        updateFestivitiesCarousel();
      } else if (targetId === 'story-section') {
        currentStoryIdx = 0;
        updateStoryCarousel();
      }

      if (typeof onCompleteCallback === 'function' && isAutoModeActive) {
        onCompleteCallback();
      }
    }, 1100);
  }

  // Handle manual scroll section transitions
  function onManualScrollCheck() {
    ensureMusicPlaying();
    if (openingState !== 'MAIN_PAGE' || isProgrammaticScrolling) return;

    const currentSec = getVisibleSectionId();
    if (currentSec !== prevVisibleSection) {
      prevVisibleSection = currentSec;
      currentSectionId = currentSec;

      if (currentSec === 'festivities-section') {
        currentFestIdx = 0;
        updateFestivitiesCarousel();
      } else if (currentSec === 'story-section') {
        currentStoryIdx = 0;
        updateStoryCarousel();
      }
    }
  }
  window.addEventListener('scroll', onManualScrollCheck, { passive: true });

  // =========================================================================
  // 4. Hero Section Typewriter Animation (Names reveal, then auto-scroll)
  // =========================================================================
  function startTypewriterAnimation() {
    const heroTop = document.querySelector('.hero-top-invocation');
    const groomChars = document.querySelectorAll('.groom-char');
    const parentsGroom = document.querySelector('.parents-line-groom');
    const ampersand = document.querySelector('.ampersand-divider');
    const brideChars = document.querySelectorAll('.bride-char');
    const parentsBride = document.querySelector('.parents-line-bride');
    const inviteRequest = document.querySelector('.hero-invitation-request');
    const scrollHint = document.querySelector('.scroll-down-hint');

    setTimeout(() => { if (heroTop) heroTop.classList.add('hero-fade-in'); }, 100);

    groomChars.forEach((ch, idx) => {
      setTimeout(() => { ch.classList.add('revealed'); }, 800 + idx * 120);
    });

    setTimeout(() => { if (parentsGroom) parentsGroom.classList.add('hero-fade-in'); }, 2200);
    setTimeout(() => { if (ampersand) ampersand.classList.add('hero-fade-in'); }, 2700);

    brideChars.forEach((ch, idx) => {
      setTimeout(() => { ch.classList.add('revealed'); }, 3100 + idx * 120);
    });

    setTimeout(() => { if (parentsBride) parentsBride.classList.add('hero-fade-in'); }, 4700);
    setTimeout(() => { if (inviteRequest) inviteRequest.classList.add('hero-fade-in'); }, 5200);

    setTimeout(() => {
      if (scrollHint) scrollHint.classList.add('hero-fade-in');

      // Auto-scroll once name animation is done: begins in 2.5 seconds
      if (sectionAdvanceTimer) clearTimeout(sectionAdvanceTimer);
      sectionAdvanceTimer = setTimeout(() => {
        if (isAutoModeActive) {
          scrollToSection('save-the-date-section', startSaveTheDateAuto);
        }
      }, 2500);
    }, 5800);
  }

  const scrollDownBtn = document.getElementById('scroll-down-hint');
  if (scrollDownBtn) {
    const handleScrollDown = (e) => {
      if (e) e.preventDefault();
      turnOffAutoScroll();
      scrollToSection('save-the-date-section');
    };
    scrollDownBtn.addEventListener('click', handleScrollDown);
    scrollDownBtn.addEventListener('touchend', handleScrollDown);
  }

  // =========================================================================
  // 5. Save the Date (Pull-to-Reveal Scroll)
  // =========================================================================
  const tasselTrigger = document.getElementById('tassel-trigger');
  const scrollParchment = document.getElementById('scroll-parchment');
  const tasselPrompt = document.getElementById('tassel-prompt');
  let isScrollUnrolled = false;

  function unrollScroll() {
    if (isScrollUnrolled) return;
    isScrollUnrolled = true;
    if (scrollParchment) scrollParchment.classList.add('unrolled');
    if (tasselPrompt) {
      tasselPrompt.innerHTML = '✦ Auspicious Date Revealed ✦';
      tasselPrompt.style.animation = 'none';
    }
    fireConfettiBurst();
  }

  function startSaveTheDateAuto() {
    if (!isAutoModeActive) return;
    if (sectionAdvanceTimer) clearTimeout(sectionAdvanceTimer);

    if (!isScrollUnrolled) {
      unrollScroll();
    }

    // Allow 2.8s for majestic slow unroll + 3.2s reading time before advancing
    sectionAdvanceTimer = setTimeout(() => {
      if (isAutoModeActive) {
        scrollToSection('festivities-section', startFestivitiesAuto);
      }
    }, 6000);
  }

  if (tasselTrigger) {
    tasselTrigger.addEventListener('click', () => {
      turnOffAutoScroll();
      unrollScroll();
    });
    let startY = 0;
    tasselTrigger.addEventListener('touchstart', (e) => {
      turnOffAutoScroll();
      startY = e.touches[0].clientY;
    }, { passive: true });
    tasselTrigger.addEventListener('touchend', (e) => {
      turnOffAutoScroll();
      const diffY = e.changedTouches[0].clientY - startY;
      if (diffY > 15 || diffY < -15) {
        unrollScroll();
      }
    }, { passive: true });
  }

  // Real-time Countdown Timer (Target: 31 Jan 2027 14:00:00 IST)
  const targetDate = new Date('2027-01-31T14:00:00+05:30').getTime();
  const elDays = document.getElementById('count-days');
  const elHours = document.getElementById('count-hours');
  const elMins = document.getElementById('count-mins');
  const elSecs = document.getElementById('count-secs');

  function updateCountdown() {
    const now = new Date().getTime();
    const distance = targetDate - now;

    if (distance <= 0) {
      if (elDays) elDays.innerText = '00';
      if (elHours) elHours.innerText = '00';
      if (elMins) elMins.innerText = '00';
      if (elSecs) elSecs.innerText = '00';
      return;
    }

    const d = Math.floor(distance / (1000 * 60 * 60 * 24));
    const h = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const m = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const s = Math.floor((distance % (1000 * 60)) / 1000);

    if (elDays) elDays.innerText = String(d).padStart(2, '0');
    if (elHours) elHours.innerText = String(h).padStart(2, '0');
    if (elMins) elMins.innerText = String(m).padStart(2, '0');
    if (elSecs) elSecs.innerText = String(s).padStart(2, '0');
  }

  setInterval(updateCountdown, 1000);
  updateCountdown();

  // Add to Calendar Button
  const addToCalBtn = document.getElementById('add-calendar-btn');
  if (addToCalBtn) {
    addToCalBtn.addEventListener('click', (e) => {
      e.preventDefault();
      turnOffAutoScroll();

      const title = encodeURIComponent("Ankit Weds Sharwani");
      const location = encodeURIComponent("Banquet Maa Jagdamba Palace, Samastipur, Bihar");
      const details = encodeURIComponent("Wedding celebration of Ankit Singh & Sharwani Singh. We look forward to celebrating together!");

      const gcalUrl = `https://calendar.google.com/calendar/render?action=TEMPLATE&text=${title}&dates=20270131T083000Z/20270131T183000Z&details=${details}&location=${location}`;

      const isIOS = /iPad|iPhone|iPod/.test(navigator.userAgent) || 
                    (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);

      if (isIOS) {
        const icsContent = [
          'BEGIN:VCALENDAR',
          'VERSION:2.0',
          'PRODID:-//Ankit weds Sharwani//Wedding//EN',
          'CALSCALE:GREGORIAN',
          'METHOD:PUBLISH',
          'BEGIN:VEVENT',
          'UID:ankit-weds-sharwani-20270131@wedding',
          'DTSTAMP:20261123T000000Z',
          'DTSTART:20270131T083000Z',
          'DTEND:20270131T183000Z',
          'SUMMARY:Ankit Weds Sharwani',
          'DESCRIPTION:Wedding celebration of Ankit Singh & Sharwani Singh. We look forward to celebrating together!',
          'LOCATION:Banquet Maa Jagdamba Palace, Samastipur, Bihar',
          'BEGIN:VALARM',
          'TRIGGER:-P1D',
          'ACTION:DISPLAY',
          'DESCRIPTION:Reminder: Ankit Weds Sharwani Tomorrow',
          'END:VALARM',
          'END:VEVENT',
          'END:VCALENDAR'
        ].join(String.fromCharCode(13, 10));

        const blob = new Blob([icsContent], { type: 'text/calendar;charset=utf-8' });
        const blobUrl = window.URL.createObjectURL(blob);
        window.location.href = blobUrl;

        setTimeout(() => {
          if (!document.hidden) {
            window.open(gcalUrl, '_blank');
          }
        }, 1500);
      } else {
        window.open(gcalUrl, '_blank');
      }
    });
  }

  // =========================================================================
  // 6. Wedding Festivities (Starts at Card 0 Lakhdav · 3s / Card · 1.2s Transition)
  // =========================================================================
  const festivityCards = document.querySelectorAll('.festivity-card');
  const festDots = document.querySelectorAll('.fest-dot');
  const festPrevBtn = document.getElementById('fest-prev-btn');
  const festNextBtn = document.getElementById('fest-next-btn');
  const festTrack = document.getElementById('festivities-track');
  let currentFestIdx = 0;
  const totalFest = festivityCards.length; // 6 cards: 0 (Lakhdav) to 5 (Baraat & Pheras)

  function updateFestivitiesCarousel() {
    festivityCards.forEach((card, idx) => {
      card.classList.remove('card-active', 'card-prev', 'card-next', 'card-hidden');
      if (idx === currentFestIdx) {
        card.classList.add('card-active');
      } else if (idx === (currentFestIdx - 1 + totalFest) % totalFest) {
        card.classList.add('card-prev');
      } else if (idx === (currentFestIdx + 1) % totalFest) {
        card.classList.add('card-next');
      } else {
        card.classList.add('card-hidden');
      }
    });

    festDots.forEach((dot, idx) => {
      dot.classList.toggle('active', idx === currentFestIdx);
    });
  }

  function startFestivitiesAuto() {
    if (!isAutoModeActive) return;
    if (cardStepTimer) clearTimeout(cardStepTimer);

    cardStepTimer = setTimeout(() => {
      if (!isAutoModeActive) return;

      if (currentFestIdx < totalFest - 1) {
        currentFestIdx++;
        updateFestivitiesCarousel();
        startFestivitiesAuto();
      } else {
        // Reached Card 5 (Baraat & Pheras) and finished 3s display!
        // Smoothly auto-scroll to Our Story!
        scrollToSection('story-section', startStoryAuto);
      }
    }, 3000);
  }

  function nextFestivity() {
    turnOffAutoScroll();
    currentFestIdx = (currentFestIdx + 1) % totalFest;
    updateFestivitiesCarousel();
  }

  function prevFestivity() {
    turnOffAutoScroll();
    currentFestIdx = (currentFestIdx - 1 + totalFest) % totalFest;
    updateFestivitiesCarousel();
  }

  if (festNextBtn) festNextBtn.addEventListener('click', nextFestivity);
  if (festPrevBtn) festPrevBtn.addEventListener('click', prevFestivity);

  festDots.forEach(dot => {
    dot.addEventListener('click', (e) => {
      turnOffAutoScroll();
      currentFestIdx = parseInt(e.target.dataset.idx);
      updateFestivitiesCarousel();
    });
  });

  // Touch Swipe on Festivities
  if (festTrack) {
    let festTouchStartX = 0;
    festTrack.addEventListener('touchstart', (e) => {
      turnOffAutoScroll();
      festTouchStartX = e.touches[0].clientX;
    }, { passive: true });
    festTrack.addEventListener('touchend', (e) => {
      turnOffAutoScroll();
      const diffX = e.changedTouches[0].clientX - festTouchStartX;
      if (diffX < -35) nextFestivity();
      else if (diffX > 35) prevFestivity();
    }, { passive: true });
  }

  // =========================================================================
  // 7. Our Story Photo Carousel (3s / Photo · 1.2s Transition)
  // =========================================================================
  const storyCards = document.querySelectorAll('.story-card');
  const storyDots = document.querySelectorAll('.story-dot');
  const storyPrevBtn = document.getElementById('story-prev-btn');
  const storyNextBtn = document.getElementById('story-next-btn');
  const storyTrack = document.getElementById('story-track');
  let currentStoryIdx = 0;
  const totalStory = storyCards.length; // 5 photos: 0 to 4

  function updateStoryCarousel() {
    storyCards.forEach((card, idx) => {
      card.classList.remove('card-active', 'card-prev', 'card-next', 'card-hidden');
      if (idx === currentStoryIdx) {
        card.classList.add('card-active');
      } else if (idx === (currentStoryIdx - 1 + totalStory) % totalStory) {
        card.classList.add('card-prev');
      } else if (idx === (currentStoryIdx + 1) % totalStory) {
        card.classList.add('card-next');
      } else {
        card.classList.add('card-hidden');
      }
    });

    storyDots.forEach((dot, idx) => {
      dot.classList.toggle('active', idx === currentStoryIdx);
    });
  }

  function startStoryAuto() {
    if (!isAutoModeActive) return;
    if (cardStepTimer) clearTimeout(cardStepTimer);

    cardStepTimer = setTimeout(() => {
      if (!isAutoModeActive) return;

      if (currentStoryIdx < totalStory - 1) {
        currentStoryIdx++;
        updateStoryCarousel();
        startStoryAuto();
      } else {
        // Photo 4 finished 3s display!
        // Smoothly auto-scroll to Grand Reception!
        scrollToSection('reception-section', startReceptionAuto);
      }
    }, 3000);
  }

  function nextStory() {
    turnOffAutoScroll();
    currentStoryIdx = (currentStoryIdx + 1) % totalStory;
    updateStoryCarousel();
  }

  function prevStory() {
    turnOffAutoScroll();
    currentStoryIdx = (currentStoryIdx - 1 + totalStory) % totalStory;
    updateStoryCarousel();
  }

  if (storyNextBtn) storyNextBtn.addEventListener('click', nextStory);
  if (storyPrevBtn) storyPrevBtn.addEventListener('click', prevStory);

  storyDots.forEach(dot => {
    dot.addEventListener('click', (e) => {
      turnOffAutoScroll();
      currentStoryIdx = parseInt(e.target.dataset.idx);
      updateStoryCarousel();
    });
  });

  // Touch Swipe on Story
  if (storyTrack) {
    let storyTouchStartX = 0;
    storyTrack.addEventListener('touchstart', (e) => {
      turnOffAutoScroll();
      storyTouchStartX = e.touches[0].clientX;
    }, { passive: true });
    storyTrack.addEventListener('touchend', (e) => {
      turnOffAutoScroll();
      const diffX = e.changedTouches[0].clientX - storyTouchStartX;
      if (diffX < -35) nextStory();
      else if (diffX > 35) prevStory();
    }, { passive: true });
  }

  // =========================================================================
  // 8. Grand Reception & How To Reach Auto-Progression
  // =========================================================================
  function startReceptionAuto() {
    if (!isAutoModeActive) return;
    if (sectionAdvanceTimer) clearTimeout(sectionAdvanceTimer);

    sectionAdvanceTimer = setTimeout(() => {
      if (isAutoModeActive) {
        scrollToSection('location-section', startLocationAuto);
      }
    }, 4500);
  }

  function startLocationAuto() {
    if (!isAutoModeActive) return;
    if (sectionAdvanceTimer) clearTimeout(sectionAdvanceTimer);

    sectionAdvanceTimer = setTimeout(() => {
      if (isAutoModeActive) {
        scrollToSection('closing-section', () => {
          // Arrived safely at footer
        });
      }
    }, 5000);
  }

  // =========================================================================
  // 9. Copy Address Toast (Handles all 3 location cards)
  // =========================================================================
  const copyToast = document.getElementById('copy-toast');
  const copyBtns = document.querySelectorAll('.copy-address-btn');

  function showToastMessage(msg) {
    if (!copyToast) return;
    copyToast.textContent = msg;
    copyToast.classList.add('show');
    setTimeout(() => {
      copyToast.classList.remove('show');
    }, 2500);
  }

  copyBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      turnOffAutoScroll();
      const address = btn.getAttribute('data-address') || 'Banquet Maa Jagdamba Palace, Samastipur, Bihar';
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(address).then(() => {
          showToastMessage('✓ ' + address + ' copied!');
        }).catch(() => fallbackCopyAddress(address));
      } else {
        fallbackCopyAddress(address);
      }
    });
  });

  function fallbackCopyAddress(address) {
    const ta = document.createElement('textarea');
    ta.value = address;
    document.body.appendChild(ta);
    ta.select();
    document.execCommand('copy');
    document.body.removeChild(ta);
    showToastMessage('✓ ' + address + ' copied!');
  }

  // =========================================================================
  // 10. Back to Top Button
  // =========================================================================
  const backToTopBtn = document.getElementById('back-to-top-btn');
  if (backToTopBtn) {
    const executeBackToTop = (e) => {
      if (e) {
        e.preventDefault();
        e.stopPropagation();
      }
      turnOffAutoScroll();

      const heroEl = document.getElementById('hero-section');
      if (heroEl) {
        heroEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
      window.scrollTo({ top: 0, left: 0, behavior: 'smooth' });
      if (document.documentElement) document.documentElement.scrollTo({ top: 0, left: 0, behavior: 'smooth' });
      if (document.body) document.body.scrollTo({ top: 0, left: 0, behavior: 'smooth' });
    };

    backToTopBtn.addEventListener('click', executeBackToTop);
    backToTopBtn.addEventListener('touchend', executeBackToTop);
  }

  // =========================================================================
  // 11. Parallax Effects: Marigold Toran & Corner Roses
  // =========================================================================
  const garlandStrings = document.querySelectorAll('.garland-string');
  const cornerDecors = document.querySelectorAll('.corner-decor');
  let lastScrollY = window.scrollY;
  let scrollVelocity = 0;
  let toranSwingAngle = 0;

  window.addEventListener('scroll', () => {
    const currentScrollY = window.scrollY;
    scrollVelocity = currentScrollY - lastScrollY;
    lastScrollY = currentScrollY;

    toranSwingAngle = Math.max(-12, Math.min(12, scrollVelocity * 0.45));
    garlandStrings.forEach((str, i) => {
      const phase = (i % 2 === 0) ? 1 : -0.7;
      str.style.transform = `rotate(${toranSwingAngle * phase}deg)`;
    });

    cornerDecors.forEach((decor) => {
      const offset = (currentScrollY * 0.04) % 15;
      decor.style.transform = `translateY(${offset}px)`;
    });
  }, { passive: true });

  setInterval(() => {
    if (Math.abs(toranSwingAngle) > 0.1) {
      toranSwingAngle *= 0.85;
      garlandStrings.forEach((str, i) => {
        const phase = (i % 2 === 0) ? 1 : -0.7;
        str.style.transform = `rotate(${toranSwingAngle * phase}deg)`;
      });
    } else {
      toranSwingAngle = 0;
      garlandStrings.forEach(str => str.style.transform = 'rotate(0deg)');
    }
  }, 50);

  // =========================================================================
  // 12. Rose Petal Shower Canvas
  // =========================================================================
  const canvas = document.getElementById('petal-canvas');
  if (canvas) {
    const ctx = canvas.getContext('2d');
    let width = canvas.width = window.innerWidth;
    let height = canvas.height = window.innerHeight;

    window.addEventListener('resize', () => {
      width = canvas.width = window.innerWidth;
      height = canvas.height = window.innerHeight;
    });

    const petalCount = 22;
    const petals = [];
    const colors = [
      { r: 192, g: 57, b: 43 },   // Crimson
      { r: 110, g: 31, b: 47 },   // Wine
      { r: 245, g: 183, b: 177 }, // Blush pink
      { r: 212, g: 175, b: 55 }   // Gold sparkle
    ];

    for (let i = 0; i < petalCount; i++) {
      petals.push({
        x: Math.random() * width,
        y: Math.random() * height - height,
        size: Math.random() * 8 + 8,
        speedX: Math.random() * 1.5 - 0.75,
        speedY: Math.random() * 1.2 + 0.8,
        rotation: Math.random() * 360,
        rotSpeed: Math.random() * 1.5 - 0.75,
        flip: Math.random() * 360,
        flipSpeed: Math.random() * 1.8 + 0.8,
        color: colors[Math.floor(Math.random() * colors.length)],
        opacity: Math.random() * 0.4 + 0.55
      });
    }

    let isTabVisible = true;
    document.addEventListener('visibilitychange', () => {
      isTabVisible = !document.hidden;
    });

    function drawPetals() {
      if (!isTabVisible) {
        requestAnimationFrame(drawPetals);
        return;
      }

      ctx.clearRect(0, 0, width, height);

      petals.forEach(p => {
        p.x += p.speedX + Math.sin(p.flip * Math.PI / 180) * 0.8;
        p.y += p.speedY;
        p.rotation += p.rotSpeed;
        p.flip += p.flipSpeed;

        if (p.y > height + 20) {
          p.y = -20;
          p.x = Math.random() * width;
        }
        if (p.x > width + 20) p.x = -20;
        if (p.x < -20) p.x = width + 20;

        ctx.save();
        ctx.translate(p.x, p.y);
        ctx.rotate(p.rotation * Math.PI / 180);
        ctx.scale(1, Math.sin(p.flip * Math.PI / 180));

        ctx.beginPath();
        ctx.moveTo(0, 0);
        ctx.bezierCurveTo(p.size / 2, -p.size / 2, p.size, 0, 0, p.size);
        ctx.bezierCurveTo(-p.size, 0, -p.size / 2, -p.size / 2, 0, 0);
        ctx.fillStyle = `rgba(${p.color.r}, ${p.color.g}, ${p.color.b}, ${p.opacity})`;
        ctx.fill();

        ctx.restore();
      });

      requestAnimationFrame(drawPetals);
    }

    drawPetals();
  }

  // =========================================================================
  // 13. Confetti Particle Burst Helper
  // =========================================================================
  function fireConfettiBurst() {
    const burstCount = 35;
    const colors = ['#D4AF37', '#FFE082', '#6E1F2F', '#C0392B', '#FFF'];
    const burstContainer = document.createElement('div');
    burstContainer.style.position = 'fixed';
    burstContainer.style.inset = '0';
    burstContainer.style.pointerEvents = 'none';
    burstContainer.style.zIndex = '99999';
    document.body.appendChild(burstContainer);

    for (let i = 0; i < burstCount; i++) {
      const conf = document.createElement('div');
      const size = Math.random() * 8 + 6;
      conf.style.position = 'absolute';
      conf.style.left = '50%';
      conf.style.top = '50%';
      conf.style.width = `${size}px`;
      conf.style.height = `${size * 0.6}px`;
      conf.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
      conf.style.borderRadius = '2px';
      conf.style.transform = 'translate(-50%, -50%)';
      burstContainer.appendChild(conf);

      const angle = Math.random() * Math.PI * 2;
      const velocity = Math.random() * 220 + 80;
      const destX = Math.cos(angle) * velocity;
      const destY = Math.sin(angle) * velocity + 100;
      const rot = Math.random() * 720;

      conf.animate([
        { transform: 'translate(-50%, -50%) rotate(0deg) scale(1)', opacity: 1 },
        { transform: `translate(calc(-50% + ${destX}px), calc(-50% + ${destY}px)) rotate(${rot}deg) scale(0.4)`, opacity: 0 }
      ], {
        duration: Math.random() * 700 + 900,
        easing: 'cubic-bezier(0.2, 0.8, 0.2, 1)'
      }).onfinish = () => conf.remove();
    }

    setTimeout(() => {
      if (burstContainer) burstContainer.remove();
    }, 1800);
  }
});
'''
