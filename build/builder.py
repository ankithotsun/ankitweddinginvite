import base64
import os
import svgs
import styles
import scripts

print("1. Loading audio & images...")
with open('References/Song_Reference.mp3', 'rb') as f:
    audio_b64 = base64.b64encode(f.read()).decode('utf-8')

images_b64 = []
for i in range(1, 6):
    with open(f'References/optimized/{i}.jpg', 'rb') as f:
        images_b64.append(base64.b64encode(f.read()).decode('utf-8'))

print("2. Generating character spans for typewriter effect...")
groom_name = "Ankit Singh"
bride_name = "Sharwani Singh"

groom_spans = "".join([f'<span class="blur-char groom-char">{c if c != " " else "&nbsp;"}</span>' for c in groom_name])
bride_spans = "".join([f'<span class="blur-char bride-char">{c if c != " " else "&nbsp;"}</span>' for c in bride_name])

print("3. Building HTML document...")

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
  <title>Ankit weds Sharwani — Wedding Invitation</title>
  
  <!-- Google Web Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700&family=Great+Vibes&family=Montserrat:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=Playfair+Display:ital,wght@0,400;0,600;0,700;0,900;1,400;1,600&display=swap" rel="stylesheet">
  
  <style>
{styles.CSS}
  </style>
</head>
<body>

  <!-- Background Music Element -->
  <audio id="bg-audio" preload="auto" loop playsinline webkit-playsinline>
    <source src="music.mp3" type="audio/mp3">
    <source src="data:audio/mp3;base64,{audio_b64}" type="audio/mp3">
  </audio>

  <!-- Rose Petal Particle Canvas -->
  <canvas id="petal-canvas"></canvas>

  <!-- Floating Audio Player Controller -->
  <div id="audio-controller" class="audio-controller" title="Play / Pause Music">
    <div class="vinyl-disc"></div>
    <div class="eq-bars">
      <div class="eq-bar"></div>
      <div class="eq-bar"></div>
      <div class="eq-bar"></div>
    </div>
    <span class="audio-label">Music</span>
  </div>

  <!-- Top Hanging Marigold Toran Garland -->
  <div class="toran-container">
    {svgs.MARIGOLD_TORAN_SVG}
  </div>

  <!-- Fixed Parallax Corner Roses -->
  <div class="corner-decor corner-top-left">{svgs.CORNER_ROSE_SVG}</div>
  <div class="corner-decor corner-top-right">{svgs.CORNER_ROSE_SVG}</div>
  <div class="corner-decor corner-bottom-left">{svgs.CORNER_ROSE_SVG}</div>
  <div class="corner-decor corner-bottom-right">{svgs.CORNER_ROSE_SVG}</div>

  <!-- ===================================================
       1. OPENING: 3D WINE-VELVET BOOK OVERLAY
       =================================================== -->
  <div id="opening-stage">
    <!-- Blurred Background Decorative Roses -->
    <div class="floating-rose-bg" style="top: 8%; left: 6%;">{svgs.CORNER_ROSE_SVG}</div>
    <div class="floating-rose-bg" style="bottom: 10%; right: 6%;">{svgs.CORNER_ROSE_SVG}</div>
    <div class="floating-rose-fg" style="top: 14%; right: 8%;">{svgs.CORNER_ROSE_SVG}</div>
    <div class="floating-rose-fg" style="bottom: 12%; left: 8%;">{svgs.CORNER_ROSE_SVG}</div>

    <!-- 3D Book Component -->
    <div id="book-wrapper" class="book-wrapper">
      <div class="book">
        <!-- Inside Back Page (Seen after opening) -->
        <div class="book-inside-page">
          <div style="width: 48px; height: 48px; margin-bottom: 12px;">{svgs.GANESH_SVG}</div>
          <p style="font-size: 11px; letter-spacing: 2px; color: var(--wine); font-weight: 600; margin-bottom: 6px;">॥ वक्रतुण्ड महाकाय सूर्यकोटि समप्रभ ॥</p>
          <p style="font-size: 10px; color: var(--text-muted); line-height: 1.6; max-width: 200px;">Two souls, one sacred bond. Welcome to our wedding celebration!</p>
        </div>

        <!-- Front Velvet Cover -->
        <div id="book-front-cover" class="book-front-cover">
          <div class="book-spine-gold"></div>
          <div class="book-embossed-border"></div>

          <div style="width: 100%; display: flex; flex-direction: column; align-items: center;">
            <p class="book-cover-shloka">॥ श्री गणेशाय नमः ॥</p>
            <div style="width: 62px; height: 62px; margin: 12px 0 6px;">{svgs.GANESH_SVG}</div>
            <p class="book-cover-title">Wedding Invitation</p>
          </div>

          <div style="width: 100%; display: flex; flex-direction: column; align-items: center;">
            <div class="book-couple-names">Ankit &amp; Sharwani</div>
            <p class="book-cover-date">31 · 01 · 2027</p>
          </div>

          <div style="width: 100%; display: flex; justify-content: center; margin-bottom: 6px;">
            <div style="font-size: 10px; letter-spacing: 2px; color: var(--gold-pale); text-transform: uppercase;">✦ Royal Union ✦</div>
          </div>
        </div>
      </div>
    </div>

    <!-- Loading State & Tap to Open Prompt -->
    <div class="tap-to-open-prompt">
      <div id="loader-container" class="loader-container">
        <div class="spinner-gold"></div>
        <span class="loader-text">Preparing your invitation...</span>
      </div>
      <div id="tap-to-open-prompt" style="display: none;">
        <button id="open-invite-btn" class="wax-seal-btn">
          <span>✨ Tap the book to open ✨</span>
        </button>
      </div>
    </div>
  </div>

  <!-- ===================================================
       MAIN MOBILE PHONE CONTAINER
       =================================================== -->
  <div class="phone-viewport">

    <!-- ===================================================
         2. FIRST PAGE: HERO SCREEN (EXACTLY 100vh)
         =================================================== -->
    <section class="hero-section" id="hero-section">
      <div class="jharokha-arch-wrapper">
        <!-- Photo #1 Blurred & Zooming Background -->
        <div class="arch-photo-bg" style="background-image: url('data:image/jpeg;base64,{images_b64[0]}');"></div>
        <div class="arch-translucent-veil"></div>
        {svgs.ARCH_TOP_SVG}
        {svgs.ARCH_BOTTOM_SVG}
      </div>

      <div class="hero-content">
        <!-- Top Ganesha & Auspicious Invocation -->
        <div class="hero-top-invocation">
          <div class="ganesh-hero-icon">{svgs.GANESH_SVG}</div>
          <p class="shloka-text">॥ श्री गणेशाय नमः ॥</p>
          <p class="family-invite-line">Together with their families</p>
        </div>

        <!-- Couple Names with Letter-by-Letter Blur-in Typewriter Effect -->
        <div class="hero-couple-block">
          <h1 class="name-groom">{groom_spans}</h1>
          <p class="parents-line parents-line-groom">Son of Smt. Mamta Devi &amp; Shri Prem Kishore Singh</p>

          <div class="ampersand-divider">
            <div class="amp-line"></div>
            <span class="amp-symbol">&amp;</span>
            <div class="amp-line"></div>
          </div>

          <h1 class="name-bride">{bride_spans}</h1>
          <p class="parents-line parents-line-bride">Daughter of Smt. Neetoo Kumari &amp; Shri Kundan Kumar Niraj</p>
        </div>

        <!-- Invitation Request & Animated Scroll Arrow -->
        <div style="display: flex; flex-direction: column; align-items: center; gap: 8px;">
          <p class="hero-invitation-request">
            Request the honour of your presence and blessings to celebrate their wedding union
          </p>

          <div id="scroll-down-hint" class="scroll-down-hint">
            <span class="scroll-text">Scroll to explore</span>
            <svg class="scroll-arrow-bouncing" viewBox="0 0 24 24">
              <path d="M7 10l5 5 5-5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </div>
        </div>
      </div>
    </section>

    <!-- ===================================================
         3. SAVE THE DATE (PULL TO REVEAL SCROLL)
         =================================================== -->
    <section class="section-container" id="save-the-date-section">
      <span class="section-badge">Auspicious Union</span>
      <h2 class="section-heading">Save The Date</h2>

      <div class="scroll-reveal-container">
        <!-- Top Golden Rod -->
        <div class="scroll-top-rod">
          <div class="rod-finial-left"></div>
          <div class="rod-finial-right"></div>
        </div>

        <!-- Unrolling Parchment -->
        <div id="scroll-parchment" class="scroll-parchment">
          <div class="scroll-border-frame"></div>
          <div class="scroll-inner-content">
            <div class="scroll-ganesh-icon">{svgs.GANESH_SVG}</div>
            <p class="save-the-date-text">SAVE THE DATE</p>
            <div class="auspicious-date-large">Sunday<br>31 January 2027</div>
            <div style="width: 40px; height: 1.5px; background: var(--gold); margin: 4px 0;"></div>
            <p class="scroll-venue-text">Banquet Maa Jagdamba Palace<br><span style="font-weight: 500; color: var(--text-muted); font-size: 11px;">Samastipur, Bihar</span></p>
          </div>
        </div>

        <!-- Bottom Rod -->
        <div class="scroll-bottom-rod"></div>

        <!-- Hanging Tassel (Interactive Trigger) -->
        <div id="tassel-trigger" class="tassel-container" title="Pull or tap to unroll scroll">
          <div class="tassel-cord"></div>
          <div class="tassel-head"></div>
          <div class="tassel-fringe"></div>
          <div id="tassel-prompt" class="tassel-prompt">
            <span>👇 Pull tassel or tap to reveal</span>
          </div>
        </div>
      </div>

      <!-- Real-time Live Countdown Clock -->
      <div class="countdown-strip">
        <div class="countdown-box">
          <span id="count-days" class="countdown-num">00</span>
          <span class="countdown-unit">Days</span>
        </div>
        <div class="countdown-box">
          <span id="count-hours" class="countdown-num">00</span>
          <span class="countdown-unit">Hours</span>
        </div>
        <div class="countdown-box">
          <span id="count-mins" class="countdown-num">00</span>
          <span class="countdown-unit">Mins</span>
        </div>
        <div class="countdown-box">
          <span id="count-secs" class="countdown-num">00</span>
          <span class="countdown-unit">Secs</span>
        </div>
      </div>

      <!-- Add to Calendar Buttons -->
      <button id="add-calendar-btn" class="calendar-action-btn">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
          <line x1="16" y1="2" x2="16" y2="6"></line>
          <line x1="8" y1="2" x2="8" y2="6"></line>
          <line x1="3" y1="10" x2="21" y2="10"></line>
        </svg>
        <span>Add to Calendar</span>
      </button>
    </section>

    <!-- ===================================================
         4. WEDDING FESTIVITIES (3D SWIPEABLE CAROUSEL)
         =================================================== -->
    <section class="section-container" id="festivities-section">
      <span class="section-badge">Celebrations &amp; Rituals</span>
      <h2 class="section-heading">Wedding Festivities</h2>

      <div class="festivities-carousel-wrapper">
        <div id="festivities-track" class="festivities-track">

          <!-- Card 1: Lakhdav -->
          <div class="festivity-card card-active" data-idx="0">
            <div class="festivity-card-scene">{svgs.SCENE_LAKHDAV}</div>
            <h3 class="festivity-name">Lakhdav</h3>
            <p class="festivity-datetime">Wednesday, 27 January 2027 · 10:00 AM</p>
            <p class="festivity-venue">At Residence - Sahebganj, Bihar</p>
            <div class="dress-code-row">
              <div class="dress-swatch" style="background: linear-gradient(135deg, #FFEAA7, #D4AF37, #C0392B);"></div>
              <span class="dress-text">Traditional · Any Festive Colour</span>
            </div>
            <a href="https://maps.app.goo.gl/GZvMXN8FQML6q38R8" target="_blank" rel="noopener" class="venue-map-link-btn">
              <span>📍 View Residence Location</span>
            </a>
          </div>

          <!-- Card 2: Tilak Cheka -->
          <div class="festivity-card card-next" data-idx="1">
            <div class="festivity-card-scene">{svgs.SCENE_TILAK}</div>
            <h3 class="festivity-name">Tilak Cheka</h3>
            <p class="festivity-datetime">Friday, 29 January 2027 · 12:00 PM</p>
            <p class="festivity-venue">At Residence - Sahebganj, Bihar</p>
            <div class="dress-code-row">
              <div class="dress-swatch" style="background: #A93226;"></div>
              <span class="dress-text">Traditional / Western · Any Colour</span>
            </div>
            <a href="https://maps.app.goo.gl/GZvMXN8FQML6q38R8" target="_blank" rel="noopener" class="venue-map-link-btn">
              <span>📍 View Residence Location</span>
            </a>
          </div>

          <!-- Card 3: Haldi -->
          <div class="festivity-card card-hidden" data-idx="2">
            <div class="festivity-card-scene">{svgs.SCENE_HALDI}</div>
            <h3 class="festivity-name">Haldi Ceremony</h3>
            <p class="festivity-datetime">Friday, 29 January 2027 · 6:00 PM</p>
            <p class="festivity-venue">At Residence - Sahebganj, Bihar</p>
            <div class="dress-code-row">
              <div class="dress-swatch" style="background: #F4B400;"></div>
              <span class="dress-text">Wear Yellow · Sunshine Shades</span>
            </div>
            <a href="https://maps.app.goo.gl/GZvMXN8FQML6q38R8" target="_blank" rel="noopener" class="venue-map-link-btn">
              <span>📍 View Residence Location</span>
            </a>
          </div>

          <!-- Card 4: Mehendi -->
          <div class="festivity-card card-hidden" data-idx="3">
            <div class="festivity-card-scene">{svgs.SCENE_MEHENDI}</div>
            <h3 class="festivity-name">Mehendi Celebration</h3>
            <p class="festivity-datetime">Friday, 29 January 2027 · 7:00 PM</p>
            <p class="festivity-venue">At Residence - Sahebganj, Bihar</p>
            <div class="dress-code-row">
              <div class="dress-swatch" style="background: #27AE60;"></div>
              <span class="dress-text">Wear Green · Henna &amp; Flora</span>
            </div>
            <a href="https://maps.app.goo.gl/GZvMXN8FQML6q38R8" target="_blank" rel="noopener" class="venue-map-link-btn">
              <span>📍 View Residence Location</span>
            </a>
          </div>

          <!-- Card 5: Sangeet -->
          <div class="festivity-card card-hidden" data-idx="4">
            <div class="festivity-card-scene">{svgs.SCENE_SANGEET}</div>
            <h3 class="festivity-name">Sangeet Night</h3>
            <p class="festivity-datetime">Friday, 29 January 2027 · 8:00 PM</p>
            <p class="festivity-venue">At Residence - Sahebganj, Bihar</p>
            <div class="dress-code-row">
              <div class="dress-swatch" style="background: linear-gradient(135deg, #8E24AA, #E91E63, #D4AF37);"></div>
              <span class="dress-text">Indo-Western · Any Colour</span>
            </div>
            <a href="https://maps.app.goo.gl/GZvMXN8FQML6q38R8" target="_blank" rel="noopener" class="venue-map-link-btn">
              <span>📍 View Residence Location</span>
            </a>
          </div>

          <!-- Card 6: Baraat & Pheras -->
          <div class="festivity-card card-prev" data-idx="5">
            <div class="festivity-card-scene">{svgs.SCENE_PHERAS}</div>
            <h3 class="festivity-name">Baraat &amp; Pheras</h3>
            <p class="festivity-datetime">Sunday, 31 January 2027 · 2:00 PM onwards</p>
            <p class="festivity-venue">From: Sahebganj to Samastipur (Banquet Palace)</p>
            <div class="dress-code-row">
              <div class="dress-swatch" style="background: linear-gradient(135deg, #C0392B, #D4AF37, #9B59B6);"></div>
              <span class="dress-text">Royal Festive / Any Colour</span>
            </div>
            <a href="https://maps.app.goo.gl/t2ieyDsWFHRwETcM7" target="_blank" rel="noopener" class="venue-map-link-btn">
              <span>📍 View Banquet Palace Location</span>
            </a>
          </div>

        </div>

        <!-- Carousel Navigation Controls -->
        <div class="carousel-nav-arrows">
          <button id="fest-prev-btn" class="carousel-btn" aria-label="Previous Festivity">‹</button>
          <div class="carousel-dots">
            <span class="dot fest-dot active" data-idx="0"></span>
            <span class="dot fest-dot" data-idx="1"></span>
            <span class="dot fest-dot" data-idx="2"></span>
            <span class="dot fest-dot" data-idx="3"></span>
            <span class="dot fest-dot" data-idx="4"></span>
            <span class="dot fest-dot" data-idx="5"></span>
          </div>
          <button id="fest-next-btn" class="carousel-btn" aria-label="Next Festivity">›</button>
        </div>
      </div>
    </section>

    <!-- ===================================================
         5. OUR STORY (3D PHOTO CAROUSEL)
         =================================================== -->
    <section class="section-container" id="story-section">
      <span class="section-badge">Memories &amp; Love</span>
      <h2 class="section-heading">Our Story</h2>

      <div class="story-carousel-wrapper">
        <div id="story-track" class="story-track">

          <!-- Photo 1 -->
          <div class="story-card card-active" data-idx="0">
            <img class="story-img" src="data:image/jpeg;base64,{images_b64[0]}" alt="Ankit & Sharwani - Where Forever Begins">
            <div class="story-caption-overlay">
              <h4 class="story-caption-title">Where Forever Begins</h4>
              <p class="story-caption-text">A gentle smile, a million unsaid promises, and a love written in the stars.</p>
            </div>
          </div>

          <!-- Photo 2 -->
          <div class="story-card card-next" data-idx="1">
            <img class="story-img" src="data:image/jpeg;base64,{images_b64[1]}" alt="Ankit & Sharwani - Every Glance, A Lifetime">
            <div class="story-caption-overlay">
              <h4 class="story-caption-title">Every Glance, A Lifetime</h4>
              <p class="story-caption-text">Finding comfort in silence, and a lifetime of happiness in each other's laughter.</p>
            </div>
          </div>

          <!-- Photo 3 -->
          <div class="story-card card-hidden" data-idx="2">
            <img class="story-img" src="data:image/jpeg;base64,{images_b64[2]}" alt="Ankit & Sharwani - Two Souls, One Destiny">
            <div class="story-caption-overlay">
              <h4 class="story-caption-title">Two Souls, One Destiny</h4>
              <p class="story-caption-text">Bound together by sacred prayers and the beautiful blessings of our families.</p>
            </div>
          </div>

          <!-- Photo 4 -->
          <div class="story-card card-hidden" data-idx="3">
            <img class="story-img" src="data:image/jpeg;base64,{images_b64[3]}" alt="Ankit & Sharwani - Hand in Hand">
            <div class="story-caption-overlay">
              <h4 class="story-caption-title">Together Through Every Season</h4>
              <p class="story-caption-text">Walking hand in hand through sunshine and rain, building our dream tomorrow.</p>
            </div>
          </div>

          <!-- Photo 5 -->
          <div class="story-card card-prev" data-idx="4">
            <img class="story-img" src="data:image/jpeg;base64,{images_b64[4]}" alt="Ankit & Sharwani - The Next Chapter">
            <div class="story-caption-overlay">
              <h4 class="story-caption-title">The Next Chapter</h4>
              <p class="story-caption-text">Step into this sacred new dawn with us, enveloped in love, joy, and blessings.</p>
            </div>
          </div>

        </div>

        <!-- Story Navigation Controls -->
        <div class="carousel-nav-arrows">
          <button id="story-prev-btn" class="carousel-btn" aria-label="Previous Story Photo">‹</button>
          <div class="carousel-dots">
            <span class="dot story-dot active" data-idx="0"></span>
            <span class="dot story-dot" data-idx="1"></span>
            <span class="dot story-dot" data-idx="2"></span>
            <span class="dot story-dot" data-idx="3"></span>
            <span class="dot story-dot" data-idx="4"></span>
          </div>
          <button id="story-next-btn" class="carousel-btn" aria-label="Next Story Photo">›</button>
        </div>
      </div>
    </section>

    <!-- ===================================================
         6. GRAND RECEPTION (DEEP WINE CARD WITH SPARKLES)
         =================================================== -->
    <section class="section-container" id="reception-section">
      <span class="section-badge">Capital City Gala</span>
      <h2 class="section-heading">Grand Reception</h2>

      <div class="reception-card-container">
        <!-- Floating Sparkle Stars -->
        <div class="reception-sparkles"></div>

        <!-- Blooming Rose Flowers in Two Corners -->
        <div class="reception-rose-topleft">{svgs.CORNER_ROSE_SVG}</div>
        <div class="reception-rose-bottomright">{svgs.CORNER_ROSE_SVG}</div>

        <p class="reception-header-tag">Celebration of Togetherness</p>
        <h3 class="reception-main-title">The Grand Reception</h3>

        <div class="reception-details-box">
          <p class="reception-line"><strong>Date:</strong> Thursday, 18 February 2027</p>
          <p class="reception-line"><strong>Time:</strong> 7:00 PM Onwards</p>
          <p class="reception-line"><strong>Venue:</strong> Tarang Banquet Hall</p>
          <p class="reception-line" style="font-size: 11.5px; color: #FFEAA7;">Ghazipur, New Delhi</p>
          <div style="width: 30px; height: 1px; background: var(--gold); margin: 6px auto;"></div>
          <p class="reception-line"><strong>Dress Code:</strong> Western Elegance / Formal</p>
        </div>
      </div>
    </section>

    <!-- ===================================================
         7. LOCATION & DIRECTIONS (3 CARDS IN SEQUENCE)
         =================================================== -->
    <section class="section-container" id="location-section">
      <span class="section-badge">Venues &amp; Navigation</span>
      <h2 class="section-heading">How To Reach</h2>

      <div class="locations-list-container">

        <!-- Card 1: Residence Location - Singh's -->
        <div class="map-card-wrapper">
          <div class="location-card-header">
            <span class="location-step-badge">1. Residence — Singh's</span>
            <span style="font-size: 11px; color: var(--gold-dark); font-weight: 600;">Family Home</span>
          </div>

          <!-- Residence Haveli Illustration -->
          {svgs.RESIDENCE_CARD_SVG}

          <div class="venue-details-block">
            <h4 class="venue-name-bold">Singh's Residence</h4>
            <p class="venue-address-sub">Sahebganj, Bihar</p>
            <p style="font-size: 10.5px; color: var(--gold-dark); margin-top: 4px; font-weight: 600;">Lakhdav · Tilak · Haldi · Mehendi · Sangeet</p>
          </div>

          <div class="map-btn-row">
            <a href="https://maps.app.goo.gl/GZvMXN8FQML6q38R8" target="_blank" rel="noopener" class="map-btn btn-directions">
              <span>🗺 Get Directions</span>
            </a>
            <button class="map-btn btn-copy-address copy-address-btn" data-address="Singh's Residence, Sahebganj, Bihar">
              <span>📋 Copy Address</span>
            </button>
          </div>
        </div>

        <!-- Card 2: Baraat Location -->
        <div class="map-card-wrapper">
          <div class="location-card-header">
            <span class="location-step-badge">2. Baraat &amp; Wedding</span>
            <span style="font-size: 11px; color: var(--gold-dark); font-weight: 600;">Main Venue</span>
          </div>

          <!-- Stylized Map Route Illustration -->
          {svgs.MAP_ROUTE_SVG}

          <div class="venue-details-block">
            <h4 class="venue-name-bold">Banquet Maa Jagdamba Palace</h4>
            <p class="venue-address-sub">Samastipur, Bihar</p>
            <p style="font-size: 10.5px; color: var(--gold-dark); margin-top: 4px; font-weight: 600;">Main Wedding Venue · Baraat &amp; Pheras</p>
          </div>

          <div class="map-btn-row">
            <a href="https://maps.app.goo.gl/t2ieyDsWFHRwETcM7" target="_blank" rel="noopener" class="map-btn btn-directions">
              <span>🗺 Get Directions</span>
            </a>
            <button class="map-btn btn-copy-address copy-address-btn" data-address="Banquet Maa Jagdamba Palace, Samastipur, Bihar">
              <span>📋 Copy Address</span>
            </button>
          </div>
        </div>

        <!-- Card 3: Reception Location - Tarang Banquet Hall -->
        <div class="map-card-wrapper">
          <div class="location-card-header">
            <span class="location-step-badge">3. Grand Reception</span>
            <span style="font-size: 11px; color: var(--gold-dark); font-weight: 600;">New Delhi</span>
          </div>

          <!-- Delhi Reception Skyline Illustration -->
          {svgs.RECEPTION_CARD_SVG}

          <div class="venue-details-block">
            <h4 class="venue-name-bold">Tarang Banquet Hall</h4>
            <p class="venue-address-sub">Ghazipur, New Delhi</p>
            <p style="font-size: 10.5px; color: var(--gold-dark); margin-top: 4px; font-weight: 600;">Post-Wedding Reception Celebration</p>
          </div>

          <div class="map-btn-row">
            <a href="https://maps.app.goo.gl/s962Zocv9gXuCNGc8" target="_blank" rel="noopener" class="map-btn btn-directions">
              <span>🗺 Get Directions</span>
            </a>
            <button class="map-btn btn-copy-address copy-address-btn" data-address="Tarang Banquet Hall, Ghazipur, New Delhi">
              <span>📋 Copy Address</span>
            </button>
          </div>
        </div>

      </div>
    </section>

    <!-- Toast Notification for Copy Address -->
    <div id="copy-toast">✓ Address copied to clipboard!</div>

    <!-- ===================================================
         8. CLOSING SECTION (FAMILY & BLESSINGS)
         =================================================== -->
    <footer class="closing-section">
      <div class="closing-ganesh">{svgs.GANESH_SVG}</div>

      <p class="closing-shloka">
        ॥ मङ्गलं भगवान् विष्णुः मङ्गलं गरुडध्वजः ।<br>
        मङ्गलं पुण्डरीकाक्षः मङ्गलाय तनो हरिः ॥
      </p>

      <h3 class="closing-heading">We can't wait to celebrate with you!</h3>

      <div style="width: 50px; height: 1.5px; background: var(--gold); margin: 6px 0 12px;"></div>

      <!-- Adults Section -->
      <div class="regards-block">
        <p class="regards-heading">With Warm Regards From</p>
        <p class="adults-members-list">
          Mohan Singh &nbsp;·&nbsp; Sunil Singh &nbsp;·&nbsp; Anil Singh &nbsp;·&nbsp; Sanjeet Singh &nbsp;·&nbsp; Ranjeet Singh &nbsp;·&nbsp; Abhay Singh &nbsp;·&nbsp; Sahil Singh
        </p>
      </div>

      <div class="regards-divider">✦ &nbsp; ✦ &nbsp; ✦</div>

      <!-- Kids / Youngsters Section (Affectionately segregated without mentioning adults/kids) -->
      <div class="regards-block">
        <p class="regards-subheading">Affectionately Awaiting Your Presence</p>
        <p class="kids-members-list">
          Avinash &nbsp;·&nbsp; Vikash &nbsp;·&nbsp; Ayush &nbsp;·&nbsp; Anuj &nbsp;·&nbsp; Anushka &nbsp;·&nbsp; Diksha &nbsp;·&nbsp; Disha &nbsp;·&nbsp; Ankush &nbsp;·&nbsp; Dikshant &nbsp;·&nbsp; Advaet &nbsp;·&nbsp; Advik &nbsp;·&nbsp; Ahan
        </p>
      </div>

      <p class="closing-family-signature">
        With love, from Singh family
      </p>

      <button id="back-to-top-btn" class="back-to-top-btn">
        <span>▲ Back to Top</span>
      </button>
    </footer>

  </div>

  <!-- Embedded Client-side Logic -->
  <script>
{scripts.JS}
  </script>
</body>
</html>
'''

print("4. Writing index.html...")
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Done! index.html written successfully ({len(html_content)} bytes).")
