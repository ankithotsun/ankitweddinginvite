# CSS Styles for Ankit & Sharwani Wedding Invitation

CSS = '''
:root {
  --wine: #6E1F2F;
  --wine-dark: #4A0D17;
  --wine-deep: #32070E;
  --wine-light: #932B40;
  --gold: #D4AF37;
  --gold-light: #FFE082;
  --gold-pale: #FFF4D0;
  --gold-dark: #8C6510;
  --ivory: #FFFDF9;
  --blush: #FBF2EF;
  --blush-deep: #F3E0DB;
  --text-dark: #382427;
  --text-muted: #73575B;
  --shadow-gold: rgba(212, 175, 55, 0.28);
  --shadow-wine: rgba(110, 31, 47, 0.25);
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  -webkit-tap-highlight-color: transparent;
}

html {
  width: 100%;
  min-height: 100%;
  scroll-behavior: smooth;
}

body {
  width: 100%;
  min-height: 100%;
  background-color: #EFE4E0;
  font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  color: var(--text-dark);
  overflow-x: hidden;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

/* Outer Desktop Frame */
.phone-viewport {
  max-width: 460px;
  min-height: 100vh;
  margin: 0 auto;
  background: var(--ivory);
  position: relative;
  box-shadow: 0 0 50px rgba(74, 13, 23, 0.35);
  overflow-x: hidden;
  display: flex;
  flex-direction: column;
}

/* Floating Audio Player Button */
.audio-controller {
  position: fixed;
  top: 18px;
  right: 18px;
  z-index: 1000;
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  background: rgba(255, 253, 249, 0.9);
  padding: 6px 10px 6px 8px;
  border-radius: 30px;
  border: 1px solid var(--gold);
  box-shadow: 0 4px 15px rgba(110, 31, 47, 0.2);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  transition: all 0.3s ease;
}

.vinyl-disc {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: radial-gradient(circle, #333 30%, #111 60%, var(--wine) 90%);
  border: 1.5px solid var(--gold);
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: transform 0.5s ease;
}

.vinyl-disc::after {
  content: '';
  width: 8px;
  height: 8px;
  background: var(--gold);
  border-radius: 50%;
}

.vinyl-disc.spinning {
  animation: discSpin 4s linear infinite;
}

@keyframes discSpin {
  100% { transform: rotate(360deg); }
}

.eq-bars {
  display: flex;
  align-items: flex-end;
  gap: 2.5px;
  height: 14px;
}

.eq-bar {
  width: 2.5px;
  background: var(--wine);
  border-radius: 2px;
  height: 4px;
  transition: height 0.2s ease;
}

.audio-playing .eq-bar:nth-child(1) { animation: eqBounce 0.9s ease-in-out infinite alternate; }
.audio-playing .eq-bar:nth-child(2) { animation: eqBounce 0.7s ease-in-out 0.2s infinite alternate; }
.audio-playing .eq-bar:nth-child(3) { animation: eqBounce 1.1s ease-in-out 0.4s infinite alternate; }

@keyframes eqBounce {
  0% { height: 3px; }
  100% { height: 14px; }
}

.audio-label {
  font-size: 10px;
  font-weight: 600;
  letter-spacing: 0.5px;
  color: var(--wine);
  text-transform: uppercase;
}

/* Top Marigold Toran */
.toran-container {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  pointer-events: none;
  z-index: 800;
  overflow: visible;
}

.toran-svg {
  width: 100%;
  height: 105px;
  display: block;
}

.garland-string {
  transition: transform 0.2s cubic-bezier(0.25, 0.8, 0.25, 1);
  will-change: transform;
}

/* Fixed Decorative Parallax Roses */
.corner-decor {
  position: fixed;
  pointer-events: none;
  z-index: 200;
  width: 90px;
  height: 90px;
  opacity: 0.88;
  will-change: transform;
  transition: transform 0.15s ease-out;
}

.corner-top-left { top: -10px; left: -10px; }
.corner-top-right { top: -10px; right: -10px; transform: scaleX(-1); }
.corner-bottom-left { bottom: -15px; left: -15px; }
.corner-bottom-right { bottom: -15px; right: -15px; transform: scaleX(-1); }

/* Rose Petal Canvas */
#petal-canvas {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 150;
}

/* ===================================================
   SECTION 1: 3D WINE-VELVET BOOK OPENING
   =================================================== */
#opening-stage {
  position: fixed;
  inset: 0;
  z-index: 9999;
  background: radial-gradient(circle at center, #FFF4F0 0%, #F5DFD8 60%, #E6C8C0 100%);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  perspective: 1400px;
  overflow: hidden;
  transition: opacity 1.8s cubic-bezier(0.4, 0, 0.2, 1), transform 2s cubic-bezier(0.4, 0, 0.2, 1);
}

#opening-stage.opened {
  opacity: 0;
  transform: scale(2.2);
  pointer-events: none;
}

.floating-rose-bg {
  position: absolute;
  pointer-events: none;
  opacity: 0.6;
  filter: blur(4px);
  animation: floatRose 8s ease-in-out infinite alternate;
}

.floating-rose-fg {
  position: absolute;
  pointer-events: none;
  opacity: 0.75;
  filter: blur(1.5px);
  animation: floatRose 6s ease-in-out 1s infinite alternate-reverse;
  z-index: 10;
}

@keyframes floatRose {
  0% { transform: translateY(0px) rotate(0deg); }
  100% { transform: translateY(-18px) rotate(8deg); }
}

.book-wrapper {
  position: relative;
  width: 290px;
  height: 430px;
  transform-style: preserve-3d;
  cursor: pointer;
  filter: drop-shadow(0 25px 40px rgba(74, 13, 23, 0.45));
}

.book {
  width: 100%;
  height: 100%;
  position: relative;
  transform-style: preserve-3d;
  border-radius: 6px 14px 14px 6px;
}

/* Inside Back Cover & Page */
.book-inside-page {
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, #FFFDF8 0%, #FAF1E8 100%);
  border-radius: 4px 12px 12px 4px;
  border: 1px solid #E2D1BE;
  padding: 30px 24px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  box-shadow: inset 18px 0 25px rgba(110, 31, 47, 0.12);
}

.book-front-cover {
  position: absolute;
  inset: 0;
  transform-origin: left center;
  transform-style: preserve-3d;
  transition: transform 2.4s cubic-bezier(0.25, 1, 0.35, 1);
  border-radius: 6px 14px 14px 6px;
  background: radial-gradient(circle at 40% 30%, #852639 0%, var(--wine) 50%, var(--wine-dark) 85%, var(--wine-deep) 100%);
  border: 1.5px solid var(--gold);
  padding: 24px 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  text-align: center;
  box-shadow: 
    inset 0 0 30px rgba(0,0,0,0.4),
    inset 8px 0 15px rgba(0,0,0,0.5),
    0 20px 45px rgba(74, 13, 23, 0.5);
  backface-visibility: hidden;
}

.book-front-cover.open-book {
  transform: rotateY(-155deg);
}

.book-embossed-border {
  position: absolute;
  inset: 10px;
  border: 1.5px solid var(--gold);
  border-radius: 4px 10px 10px 4px;
  pointer-events: none;
}

.book-embossed-border::after {
  content: '';
  position: absolute;
  inset: 4px;
  border: 0.8px dashed rgba(255, 224, 130, 0.7);
  border-radius: 2px 8px 8px 2px;
}

.book-spine-gold {
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  width: 14px;
  background: linear-gradient(90deg, rgba(0,0,0,0.4) 0%, rgba(212,175,55,0.4) 50%, rgba(0,0,0,0.3) 100%);
  border-radius: 6px 0 0 6px;
}

.book-cover-shloka {
  font-size: 11px;
  letter-spacing: 2px;
  color: var(--gold-light);
  font-weight: 500;
  margin-top: 8px;
  text-shadow: 0 1px 3px rgba(0,0,0,0.5);
}

.book-cover-title {
  font-family: 'Cinzel Decorative', 'Playfair Display', serif;
  font-size: 13px;
  letter-spacing: 3px;
  color: var(--gold-pale);
  text-transform: uppercase;
  margin-top: 10px;
  text-shadow: 0 1px 4px rgba(0,0,0,0.6);
}

.book-couple-names {
  font-family: 'Great Vibes', cursive;
  font-size: 38px;
  color: #FFF2A3;
  line-height: 1.15;
  background: linear-gradient(135deg, #FFF9D2 0%, #F5D77F 40%, #E5A93C 70%, #FFF2A3 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  filter: drop-shadow(0 2px 6px rgba(0,0,0,0.6));
  margin: 6px 0;
}

.book-cover-date {
  font-size: 11.5px;
  letter-spacing: 3px;
  color: var(--gold-light);
  font-weight: 600;
  margin-bottom: 8px;
}

/* Loader & Tap to Open Prompt */
.tap-to-open-prompt {
  margin-top: 24px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
}

.wax-seal-btn {
  background: linear-gradient(135deg, #E5B53C 0%, #D4AF37 50%, #996515 100%);
  color: var(--wine-deep);
  border: none;
  padding: 10px 22px;
  border-radius: 25px;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  cursor: pointer;
  box-shadow: 0 6px 20px rgba(212, 175, 55, 0.4), 0 0 15px rgba(255, 235, 150, 0.5);
  display: flex;
  align-items: center;
  gap: 8px;
  animation: pulseGlow 2s infinite alternate;
}

@keyframes pulseGlow {
  0% { transform: scale(1); box-shadow: 0 4px 15px rgba(212,175,55,0.4); }
  100% { transform: scale(1.05); box-shadow: 0 8px 25px rgba(212,175,55,0.7), 0 0 20px rgba(255,235,150,0.8); }
}

.loader-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
}

.spinner-gold {
  width: 32px;
  height: 32px;
  border: 2.5px solid rgba(212, 175, 55, 0.2);
  border-top-color: var(--gold);
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  100% { transform: rotate(360deg); }
}

.loader-text {
  font-size: 11px;
  letter-spacing: 1px;
  color: var(--wine);
  font-weight: 600;
}

/* ===================================================
   SECTION 2: FIRST PAGE (HERO SECTION - EXACTLY 100vh)
   =================================================== */
.hero-section {
  width: 100%;
  height: 100vh;
  height: 100svh;
  height: 100dvh;
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  text-align: center;
  padding: 18px 16px 22px;
  box-sizing: border-box;
  background: var(--ivory);
  overflow: hidden;
}

.jharokha-arch-wrapper {
  position: absolute;
  inset: 12px;
  border-radius: 20px;
  border: 1.5px solid var(--gold);
  box-shadow: 
    0 12px 35px rgba(110, 31, 47, 0.2),
    inset 0 0 0 3px rgba(255, 253, 249, 0.6),
    inset 0 0 0 4.5px rgba(212, 175, 55, 0.65);
  overflow: hidden;
  z-index: 1;
}

.arch-photo-bg {
  position: absolute;
  inset: 0;
  background-size: cover;
  background-position: center 38%;
  filter: blur(1.5px) brightness(0.94);
  transform: scale(1.08);
  animation: subtleZoom 20s ease-in-out infinite alternate;
}

@keyframes subtleZoom {
  0% { transform: scale(1.05) translate(0, 0); }
  100% { transform: scale(1.16) translate(-1%, -2%); }
}

.arch-translucent-veil {
  position: absolute;
  inset: 0;
  background: radial-gradient(
    ellipse at 50% 48%,
    rgba(255, 253, 249, 0.38) 0%,
    rgba(253, 245, 242, 0.52) 50%,
    rgba(247, 228, 222, 0.72) 100%
  );
  backdrop-filter: blur(0.5px);
  -webkit-backdrop-filter: blur(0.5px);
}

.arch-top-svg {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 155px;
  pointer-events: none;
  z-index: 5;
}

.arch-bottom-svg {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 40px;
  pointer-events: none;
  z-index: 5;
}

.hero-content {
  position: relative;
  z-index: 10;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  padding: 24px 14px 10px;
}

.hero-top-invocation {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
}

.ganesh-hero-icon {
  width: 52px;
  height: 52px;
  filter: drop-shadow(0 2px 8px rgba(212, 175, 55, 0.5));
}

.shloka-text {
  font-size: 11px;
  letter-spacing: 2px;
  color: var(--wine);
  font-weight: 600;
}

.family-invite-line {
  font-size: 10.5px;
  letter-spacing: 2px;
  color: var(--text-muted);
  text-transform: uppercase;
  font-weight: 500;
  margin-top: 2px;
}

.hero-couple-block {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2px;
  margin: auto 0;
}

.name-groom, .name-bride {
  font-family: 'Playfair Display', serif;
  font-size: 32px;
  font-weight: 700;
  letter-spacing: 0.5px;
  color: var(--wine);
  line-height: 1.15;
  text-shadow: 
    0 1px 4px rgba(255, 255, 255, 0.98), 
    0 0 16px rgba(255, 253, 249, 0.95),
    0 2px 8px rgba(255, 255, 255, 0.9);
}

.parents-line {
  font-size: 11.5px;
  color: var(--text-dark);
  font-weight: 600;
  margin-top: 3px;
  text-shadow: 0 1px 3px rgba(255, 255, 255, 0.95), 0 0 8px rgba(255, 255, 255, 0.85);
}

.ampersand-divider {
  display: flex;
  align-items: center;
  gap: 8px;
  margin: 6px 0;
}

.amp-line {
  width: 25px;
  height: 1px;
  background: linear-gradient(90deg, transparent, var(--gold), transparent);
}

.amp-symbol {
  font-family: 'Great Vibes', cursive;
  font-size: 26px;
  color: var(--gold);
}

.hero-invitation-request {
  font-size: 11px;
  line-height: 1.5;
  color: var(--text-dark);
  font-weight: 500;
  max-width: 280px;
  margin: 4px auto 0;
}

/* Blur-in Typewriter Effect - Slow & Elegant */
.blur-char {
  display: inline-block;
  opacity: 0;
  filter: blur(10px);
  transform: translateY(6px);
  transition: opacity 0.8s cubic-bezier(0.2, 0.8, 0.2, 1), 
              filter 0.8s cubic-bezier(0.2, 0.8, 0.2, 1), 
              transform 0.8s cubic-bezier(0.2, 0.8, 0.2, 1);
}

.blur-char.revealed {
  opacity: 1;
  filter: blur(0);
  transform: translateY(0);
}

.hero-top-invocation,
.parents-line,
.ampersand-divider,
.hero-invitation-request,
.scroll-down-hint {
  opacity: 0;
  filter: blur(8px);
  transform: translateY(6px);
  transition: opacity 0.9s cubic-bezier(0.2, 0.8, 0.2, 1),
              filter 0.9s cubic-bezier(0.2, 0.8, 0.2, 1),
              transform 0.9s cubic-bezier(0.2, 0.8, 0.2, 1);
}

.hero-top-invocation.hero-fade-in,
.parents-line.hero-fade-in,
.ampersand-divider.hero-fade-in,
.hero-invitation-request.hero-fade-in,
.scroll-down-hint.hero-fade-in {
  opacity: 1;
  filter: blur(0);
  transform: translateY(0);
}

/* Scroll Down Hint */
.scroll-down-hint {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  cursor: pointer;
  margin-bottom: 4px;
}

.scroll-text {
  font-size: 9.5px;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: var(--wine);
  font-weight: 600;
}

.scroll-arrow-bouncing {
  width: 18px;
  height: 18px;
  stroke: var(--wine);
  stroke-width: 2;
  fill: none;
  animation: bounceDown 1.8s infinite;
}

@keyframes bounceDown {
  0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
  40% { transform: translateY(6px); }
  60% { transform: translateY(3px); }
}

/* ===================================================
   SECTION 3: SAVE THE DATE (PULL TO REVEAL SCROLL)
   =================================================== */
.section-container {
  padding: 45px 20px;
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.section-badge {
  font-size: 10px;
  letter-spacing: 2.5px;
  text-transform: uppercase;
  color: var(--gold-dark);
  font-weight: 700;
  margin-bottom: 6px;
}

.section-heading {
  font-family: 'Playfair Display', serif;
  font-size: 26px;
  font-weight: 700;
  color: var(--wine);
  margin-bottom: 18px;
}

.scroll-reveal-container {
  width: 100%;
  max-width: 380px;
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
}

.scroll-top-rod {
  width: 100%;
  height: 14px;
  background: linear-gradient(90deg, #7A5210 0%, #D4AF37 30%, #FFF2A3 50%, #D4AF37 70%, #7A5210 100%);
  border-radius: 7px;
  position: relative;
  box-shadow: 0 4px 10px rgba(0,0,0,0.25);
  z-index: 20;
}

.rod-finial-left, .rod-finial-right {
  position: absolute;
  top: -4px;
  width: 12px;
  height: 22px;
  background: linear-gradient(135deg, #FFEAA7, #D4AF37, #8C6510);
  border-radius: 4px;
}

.rod-finial-left { left: -8px; border-radius: 6px 0 0 6px; }
.rod-finial-right { right: -8px; border-radius: 0 6px 6px 0; }

.scroll-parchment {
  width: 90%;
  background: linear-gradient(180deg, #FFFDF8 0%, #FAF0E4 50%, #F5E8D8 100%);
  border-left: 2px solid var(--gold);
  border-right: 2px solid var(--gold);
  box-shadow: 0 4px 15px rgba(110, 31, 47, 0.08);
  max-height: 0;
  overflow: hidden;
  transition: max-height 2.8s cubic-bezier(0.35, 0.05, 0.2, 1), box-shadow 2.8s ease;
  position: relative;
}

.scroll-parchment.unrolled {
  max-height: 335px;
  box-shadow: 0 16px 35px rgba(110, 31, 47, 0.2);
}

.scroll-inner-content {
  padding: 24px 18px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
  opacity: 0;
  transform: translateY(-18px);
  filter: blur(1.5px);
  transition: opacity 2.2s cubic-bezier(0.35, 0.05, 0.2, 1) 0.3s,
              transform 2.4s cubic-bezier(0.35, 0.05, 0.2, 1) 0.2s,
              filter 2.0s ease 0.3s;
}

.scroll-parchment.unrolled .scroll-inner-content {
  opacity: 1;
  transform: translateY(0);
  filter: blur(0px);
}

.scroll-border-frame {
  position: absolute;
  inset: 8px;
  border: 1px solid rgba(212, 175, 55, 0.6);
  border-radius: 4px;
  pointer-events: none;
}

.scroll-ganesh-icon {
  width: 44px;
  height: 44px;
}

.save-the-date-text {
  font-family: 'Cinzel Decorative', serif;
  font-size: 14px;
  letter-spacing: 4px;
  color: var(--gold-dark);
  font-weight: 700;
}

.auspicious-date-large {
  font-family: 'Playfair Display', serif;
  font-size: 27px;
  font-weight: 700;
  color: var(--wine);
  line-height: 1.2;
}

.scroll-venue-text {
  font-size: 12px;
  font-weight: 600;
  color: var(--text-dark);
}

.scroll-bottom-rod {
  width: 92%;
  height: 12px;
  background: linear-gradient(90deg, #7A5210 0%, #D4AF37 30%, #FFF2A3 50%, #D4AF37 70%, #7A5210 100%);
  border-radius: 6px;
  box-shadow: 0 4px 10px rgba(0,0,0,0.2);
  position: relative;
  z-index: 15;
}

/* Tassel & Pull Prompt */
.tassel-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  cursor: pointer;
  margin-top: 4px;
  transform-origin: top center;
  animation: slowTasselSwing 3.6s infinite ease-in-out;
  transition: transform 0.3s ease;
}

@keyframes slowTasselSwing {
  0%, 100% { transform: translateY(0) rotate(0deg); }
  25% { transform: translateY(2.5px) rotate(2deg); }
  50% { transform: translateY(0) rotate(0deg); }
  75% { transform: translateY(2.5px) rotate(-2deg); }
}

.tassel-cord {
  width: 2px;
  height: 18px;
  background: var(--gold);
}

.tassel-head {
  width: 10px;
  height: 10px;
  background: linear-gradient(135deg, #FFEAA7, #D4AF37);
  border-radius: 50%;
}

.tassel-fringe {
  width: 16px;
  height: 24px;
  background: linear-gradient(180deg, #D4AF37 0%, #AA771C 100%);
  clip-path: polygon(25% 0%, 75% 0%, 100% 100%, 0% 100%);
}

.tassel-prompt {
  margin-top: 10px;
  display: flex;
  align-items: center;
  gap: 6px;
  background: rgba(255, 253, 249, 0.95);
  border: 1px solid var(--gold);
  padding: 6px 14px;
  border-radius: 20px;
  font-size: 11px;
  font-weight: 600;
  color: var(--wine);
  box-shadow: 0 4px 12px rgba(110, 31, 47, 0.12);
  animation: bounceTassel 3.6s infinite ease-in-out;
}

@keyframes bounceTassel {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(3.5px); }
}

/* Countdown Clock Strip */
.countdown-strip {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  margin: 22px 0 16px;
}

.countdown-box {
  background: linear-gradient(135deg, #FFFDF8 0%, #FAF0E4 100%);
  border: 1px solid var(--gold);
  border-radius: 8px;
  padding: 8px 10px;
  min-width: 58px;
  box-shadow: 0 4px 12px rgba(110, 31, 47, 0.1);
  display: flex;
  flex-direction: column;
  align-items: center;
}

.countdown-num {
  font-family: 'Playfair Display', serif;
  font-size: 20px;
  font-weight: 700;
  color: var(--wine);
  line-height: 1;
}

.countdown-unit {
  font-size: 9px;
  text-transform: uppercase;
  letter-spacing: 1px;
  color: var(--text-muted);
  font-weight: 600;
  margin-top: 3px;
}

.calendar-action-btn {
  background: linear-gradient(135deg, #6E1F2F 0%, #4A0D17 100%);
  color: #FFFDF9;
  border: 1px solid var(--gold);
  padding: 10px 22px;
  border-radius: 25px;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.5px;
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  box-shadow: 0 4px 15px rgba(110, 31, 47, 0.3);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.calendar-action-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(110, 31, 47, 0.4);
}

/* ===================================================
   SECTION 4: WEDDING FESTIVITIES (SWIPEABLE 3D CAROUSEL)
   =================================================== */
.festivities-carousel-wrapper {
  width: 100%;
  position: relative;
  overflow: hidden;
  padding: 15px 0 25px;
  perspective: 1200px;
}

.festivities-track {
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  min-height: 380px;
  width: 100%;
  touch-action: pan-y;
}

.festivity-card {
  position: absolute;
  width: 285px;
  background: linear-gradient(135deg, #FFFDF9 0%, #FDF6F3 100%);
  border: 1.5px solid var(--gold);
  border-radius: 18px;
  padding: 22px 18px;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  box-shadow: 0 15px 35px rgba(110, 31, 47, 0.15);
  transition: transform 1.2s cubic-bezier(0.25, 1, 0.35, 1), opacity 1.2s cubic-bezier(0.25, 1, 0.35, 1), filter 1.2s cubic-bezier(0.25, 1, 0.35, 1);
  will-change: transform, opacity, filter;
  cursor: grab;
}

.festivity-card.card-active {
  transform: translateX(0) scale(1) rotate(0deg);
  opacity: 1;
  z-index: 10;
  filter: blur(0);
}

.festivity-card.card-prev {
  transform: translateX(-72%) scale(0.85) rotate(-2.5deg);
  opacity: 0.5;
  z-index: 5;
  filter: blur(1.5px);
  pointer-events: none;
}

.festivity-card.card-next {
  transform: translateX(72%) scale(0.85) rotate(2.5deg);
  opacity: 0.5;
  z-index: 5;
  filter: blur(1.5px);
  pointer-events: none;
}

.festivity-card.card-hidden {
  transform: translateX(120%) scale(0.7) rotate(5deg);
  opacity: 0;
  z-index: 1;
  pointer-events: none;
}

.festivity-card-scene {
  width: 100%;
  height: 95px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 8px;
}

.scene-illustration {
  width: 110px;
  height: 85px;
}

.festivity-name {
  font-family: 'Playfair Display', serif;
  font-size: 21px;
  font-weight: 700;
  color: var(--wine);
  margin-bottom: 4px;
}

.festivity-datetime {
  font-size: 11.5px;
  font-weight: 600;
  color: var(--gold-dark);
  margin-bottom: 2px;
}

.festivity-venue {
  font-size: 11px;
  color: var(--text-dark);
  font-weight: 500;
  margin-bottom: 12px;
}

.dress-code-row {
  display: flex;
  align-items: center;
  gap: 8px;
  background: rgba(251, 242, 239, 0.8);
  padding: 6px 12px;
  border-radius: 20px;
  border: 1px solid rgba(212, 175, 55, 0.4);
  margin-bottom: 14px;
}

.dress-swatch {
  width: 14px;
  height: 14px;
  border-radius: 50%;
  border: 1.5px solid #FFF;
  box-shadow: 0 0 4px rgba(0,0,0,0.2);
}

.dress-text {
  font-size: 10.5px;
  font-weight: 600;
  color: var(--text-dark);
}

.venue-map-link-btn {
  font-size: 11px;
  font-weight: 600;
  color: var(--wine);
  text-decoration: none;
  display: flex;
  align-items: center;
  gap: 4px;
  padding: 5px 12px;
  border-radius: 15px;
  background: #FFF;
  border: 1px solid var(--wine);
  transition: all 0.2s ease;
}

.carousel-nav-arrows {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 20px;
  margin-top: 15px;
}

.carousel-btn {
  width: 38px;
  height: 38px;
  border-radius: 50%;
  background: #FFF;
  border: 1px solid var(--gold);
  color: var(--wine);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px;
  font-weight: 700;
  cursor: pointer;
  box-shadow: 0 4px 10px rgba(110, 31, 47, 0.12);
  transition: all 0.2s ease;
}

.carousel-btn:hover {
  background: var(--wine);
  color: #FFF;
}

.carousel-dots {
  display: flex;
  gap: 6px;
}

.dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: #D9C3BA;
  cursor: pointer;
  transition: all 0.3s ease;
}

.dot.active {
  width: 20px;
  border-radius: 10px;
  background: var(--wine);
}

/* ===================================================
   SECTION 5: OUR STORY (3D PHOTO CAROUSEL)
   =================================================== */
.story-carousel-wrapper {
  width: 100%;
  position: relative;
  overflow: hidden;
  padding: 15px 0 25px;
  perspective: 1200px;
}

.story-track {
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  min-height: 440px;
  width: 100%;
  touch-action: pan-y;
}

.story-card {
  position: absolute;
  width: 275px;
  height: 410px;
  border-radius: 18px;
  overflow: hidden;
  border: 2px solid var(--gold);
  box-shadow: 0 18px 40px rgba(110, 31, 47, 0.25);
  transition: transform 1.2s cubic-bezier(0.25, 1, 0.35, 1), opacity 1.2s cubic-bezier(0.25, 1, 0.35, 1), filter 1.2s cubic-bezier(0.25, 1, 0.35, 1);
  will-change: transform, opacity, filter;
  cursor: grab;
}

.story-card.card-active {
  transform: translateX(0) scale(1) rotate(0deg);
  opacity: 1;
  z-index: 10;
  filter: blur(0);
}

.story-card.card-prev {
  transform: translateX(-72%) scale(0.85) rotate(-2.5deg);
  opacity: 0.5;
  z-index: 5;
  filter: blur(1.5px);
  pointer-events: none;
}

.story-card.card-next {
  transform: translateX(72%) scale(0.85) rotate(2.5deg);
  opacity: 0.5;
  z-index: 5;
  filter: blur(1.5px);
  pointer-events: none;
}

.story-card.card-hidden {
  transform: translateX(120%) scale(0.7) rotate(5deg);
  opacity: 0;
  z-index: 1;
  pointer-events: none;
}

.story-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.story-caption-overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background: linear-gradient(180deg, transparent 0%, rgba(50, 7, 14, 0.75) 40%, rgba(50, 7, 14, 0.95) 100%);
  padding: 30px 16px 18px;
  color: #FFF;
  text-align: center;
  backdrop-filter: blur(2px);
  -webkit-backdrop-filter: blur(2px);
}

.story-caption-title {
  font-family: 'Playfair Display', serif;
  font-size: 17px;
  font-weight: 700;
  color: #FFF2A3;
  margin-bottom: 4px;
}

.story-caption-text {
  font-size: 11px;
  color: #F8E8E8;
  font-weight: 400;
  line-height: 1.4;
}

/* ===================================================
   SECTION 6: GRAND RECEPTION
   =================================================== */
.reception-card-container {
  width: 100%;
  max-width: 380px;
  position: relative;
  background: radial-gradient(circle at center, #7C1D30 0%, var(--wine) 50%, var(--wine-dark) 85%, var(--wine-deep) 100%);
  border: 1.8px solid var(--gold);
  border-radius: 20px;
  padding: 35px 22px;
  box-shadow: 0 20px 45px rgba(74, 13, 23, 0.4), inset 0 0 30px rgba(0,0,0,0.4);
  color: #FFFDF9;
  text-align: center;
  overflow: hidden;
}

.reception-sparkles {
  position: absolute;
  inset: 0;
  pointer-events: none;
  background-image: 
    radial-gradient(1.5px 1.5px at 20px 30px, #FFF, rgba(0,0,0,0)),
    radial-gradient(1.5px 1.5px at 150px 80px, #FFEAA7, rgba(0,0,0,0)),
    radial-gradient(2px 2px at 290px 40px, #FFF, rgba(0,0,0,0)),
    radial-gradient(1.5px 1.5px at 80px 220px, #FFEAA7, rgba(0,0,0,0)),
    radial-gradient(2px 2px at 300px 260px, #FFF, rgba(0,0,0,0));
  background-repeat: repeat;
  background-size: 320px 320px;
  animation: sparkleTwinkle 4s ease-in-out infinite alternate;
}

@keyframes sparkleTwinkle {
  0% { opacity: 0.4; }
  100% { opacity: 0.95; }
}

.reception-rose-topleft {
  position: absolute;
  top: -8px;
  left: -8px;
  width: 75px;
  height: 75px;
  pointer-events: none;
  filter: drop-shadow(0 4px 8px rgba(0,0,0,0.5));
}

.reception-rose-bottomright {
  position: absolute;
  bottom: -8px;
  right: -8px;
  width: 75px;
  height: 75px;
  pointer-events: none;
  transform: rotate(180deg);
  filter: drop-shadow(0 4px 8px rgba(0,0,0,0.5));
}

.reception-header-tag {
  font-family: 'Cinzel Decorative', serif;
  font-size: 12px;
  letter-spacing: 3px;
  color: var(--gold-pale);
  text-transform: uppercase;
}

.reception-main-title {
  font-family: 'Playfair Display', serif;
  font-size: 26px;
  font-weight: 700;
  color: #FFF2A3;
  margin: 8px 0 12px;
}

.reception-details-box {
  background: rgba(0, 0, 0, 0.25);
  border: 1px solid rgba(212, 175, 55, 0.4);
  border-radius: 12px;
  padding: 14px 12px;
  margin: 14px 0 20px;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.reception-line {
  font-size: 12px;
  color: #FBF2EF;
}

.reception-line strong {
  color: #FFF2A3;
  font-weight: 600;
}

.reception-action-btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: linear-gradient(135deg, #FFE082 0%, #D4AF37 50%, #996515 100%);
  color: var(--wine-deep);
  text-decoration: none;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.5px;
  padding: 10px 22px;
  border-radius: 25px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4);
  transition: transform 0.2s ease;
}

/* ===================================================
   SECTION 7: LOCATION & DIRECTIONS (3 CARDS IN SEQUENCE)
   =================================================== */
.locations-list-container {
  display: flex;
  flex-direction: column;
  gap: 22px;
  width: 100%;
  max-width: 390px;
  align-items: center;
}

.map-card-wrapper {
  width: 100%;
  background: #FFFDF9;
  border: 1.5px solid var(--gold);
  border-radius: 18px;
  padding: 20px 16px;
  box-shadow: 0 12px 30px rgba(110, 31, 47, 0.12);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
  position: relative;
}

.location-card-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  padding-bottom: 2px;
}

.location-step-badge {
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 1px;
  text-transform: uppercase;
  color: var(--wine);
  background: rgba(110, 31, 47, 0.08);
  border: 1px solid rgba(110, 31, 47, 0.2);
  padding: 3px 10px;
  border-radius: 12px;
}

.map-route-svg {
  width: 100%;
  height: auto;
  border-radius: 10px;
}

.pulse-ring {
  animation: pulsePin 1.8s infinite;
}

@keyframes pulsePin {
  0% { r: 6; opacity: 0.8; }
  100% { r: 14; opacity: 0; }
}

.animated-route-line {
  stroke-dashoffset: 100;
  animation: dashRoute 8s linear infinite;
}

@keyframes dashRoute {
  to { stroke-dashoffset: 0; }
}

.venue-details-block {
  text-align: center;
}

.venue-name-bold {
  font-family: 'Playfair Display', serif;
  font-size: 17px;
  font-weight: 700;
  color: var(--wine);
  margin-bottom: 4px;
}

.venue-address-sub {
  font-size: 11.5px;
  color: var(--text-muted);
  line-height: 1.4;
}

.map-btn-row {
  display: flex;
  gap: 10px;
  width: 100%;
  justify-content: center;
}

.map-btn {
  flex: 1;
  padding: 9px 12px;
  border-radius: 20px;
  font-size: 11px;
  font-weight: 600;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  cursor: pointer;
  text-decoration: none;
  transition: all 0.2s ease;
}

.btn-directions {
  background: var(--wine);
  color: #FFF;
  border: 1px solid var(--wine);
}

.btn-copy-address {
  background: #FFF;
  color: var(--wine);
  border: 1px solid var(--wine);
}

/* Toast Message */
#copy-toast {
  position: fixed;
  bottom: 30px;
  left: 50%;
  transform: translateX(-50%) translateY(40px);
  background: rgba(50, 7, 14, 0.95);
  color: #FFF2A3;
  border: 1px solid var(--gold);
  padding: 10px 20px;
  border-radius: 25px;
  font-size: 12px;
  font-weight: 600;
  box-shadow: 0 6px 20px rgba(0,0,0,0.4);
  opacity: 0;
  pointer-events: none;
  transition: all 0.3s cubic-bezier(0.2, 0.8, 0.2, 1);
  z-index: 2000;
}

#copy-toast.show {
  opacity: 1;
  transform: translateX(-50%) translateY(0);
}

/* ===================================================
   SECTION 8: CLOSING SECTION (FAMILY & BLESSINGS)
   =================================================== */
.closing-section {
  padding: 50px 20px 70px;
  background: linear-gradient(180deg, var(--ivory) 0%, #FAF0EB 100%);
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: 14px;
  position: relative;
}

.closing-ganesh {
  width: 48px;
  height: 48px;
}

.closing-shloka {
  font-size: 11.5px;
  line-height: 1.7;
  color: var(--wine);
  font-weight: 600;
  max-width: 320px;
}

.closing-heading {
  font-family: 'Playfair Display', serif;
  font-size: 22px;
  font-weight: 700;
  color: var(--wine);
  margin-top: 6px;
}

.regards-block {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  max-width: 380px;
}

.regards-heading {
  font-family: 'Montserrat', sans-serif;
  font-size: 11px;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: var(--gold-dark);
  font-weight: 700;
}

.adults-members-list {
  font-family: 'Playfair Display', serif;
  font-size: 14px;
  font-weight: 600;
  color: var(--wine);
  line-height: 1.8;
  letter-spacing: 0.3px;
}

.regards-divider {
  font-size: 10px;
  letter-spacing: 6px;
  color: var(--gold);
  margin: 4px 0;
  opacity: 0.85;
}

.regards-subheading {
  font-size: 10.5px;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: var(--text-muted);
  font-weight: 600;
}

.kids-members-list {
  font-family: 'Montserrat', sans-serif;
  font-size: 12px;
  font-weight: 500;
  color: var(--text-dark);
  line-height: 1.8;
  letter-spacing: 0.4px;
}

.closing-family-signature {
  font-family: 'Great Vibes', cursive;
  font-size: 30px;
  color: var(--wine);
  margin-top: 10px;
}

/* Back to Top Floating Button */
.back-to-top-btn {
  margin-top: 25px;
  background: transparent;
  border: 1px solid var(--gold);
  color: var(--wine);
  padding: 8px 18px;
  border-radius: 20px;
  font-size: 10.5px;
  font-weight: 600;
  letter-spacing: 1px;
  text-transform: uppercase;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 6px;
  transition: all 0.2s ease;
  position: relative;
  z-index: 50;
  pointer-events: auto;
  user-select: none;
  -webkit-user-select: none;
}

.back-to-top-btn:active {
  transform: scale(0.96);
  background: rgba(212, 175, 55, 0.15);
}

.back-to-top-btn:hover {
  background: var(--wine);
  color: #FFF;
}
'''
