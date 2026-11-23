# High quality SVG definitions for Ankit & Sharwani Wedding Invitation

GANESH_SVG = '''
<svg class="ganesh-svg" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="gGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FFF5B8" stop-opacity="0.9"/>
      <stop offset="55%" stop-color="#D4AF37" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#8C6510" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="gGold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFF3C4"/>
      <stop offset="25%" stop-color="#F7D070"/>
      <stop offset="50%" stop-color="#D4AF37"/>
      <stop offset="75%" stop-color="#AA771C"/>
      <stop offset="100%" stop-color="#5E400B"/>
    </linearGradient>
  </defs>
  <!-- Divine Aura -->
  <circle cx="50" cy="50" r="48" fill="url(#gGlow)" class="ganesh-aura"/>
  <circle cx="50" cy="50" r="45" fill="none" stroke="url(#gGold)" stroke-width="1.2" stroke-dasharray="3 3"/>
  <circle cx="50" cy="50" r="42" fill="none" stroke="url(#gGold)" stroke-width="0.8"/>
  
  <!-- Crown / Mukut -->
  <path d="M43 23 L50 10 L57 23 L53 27 L47 27 Z" fill="url(#gGold)" stroke="#6E1F2F" stroke-width="0.5"/>
  <circle cx="50" cy="10" r="2.2" fill="#FFEAA7"/>
  <circle cx="50" cy="18" r="1.4" fill="#C0392B"/>
  
  <!-- Ears -->
  <path d="M42 28 C28 24 23 37 28 47 C32 52 38 49 41 44" fill="none" stroke="url(#gGold)" stroke-width="2.6" stroke-linecap="round"/>
  <path d="M58 28 C72 24 77 37 72 47 C68 52 62 49 59 44" fill="none" stroke="url(#gGold)" stroke-width="2.6" stroke-linecap="round"/>
  
  <!-- Forehead & Tilak -->
  <path d="M42 28 C45 25 55 25 58 28" fill="none" stroke="url(#gGold)" stroke-width="2.4"/>
  <path d="M47 27 C47 34 50 36 50 36 C50 36 53 34 53 27" fill="none" stroke="#C0392B" stroke-width="1.5"/>
  <line x1="50" y1="24" x2="50" y2="35" stroke="#C0392B" stroke-width="1.2"/>
  <circle cx="50" cy="38" r="1.3" fill="#C0392B"/>
  
  <!-- Eyes -->
  <path d="M40 33 Q44 35 46 33" fill="none" stroke="#6E1F2F" stroke-width="1.4" stroke-linecap="round"/>
  <path d="M60 33 Q56 35 54 33" fill="none" stroke="#6E1F2F" stroke-width="1.4" stroke-linecap="round"/>
  
  <!-- Tusks -->
  <path d="M44 44 L39 46" stroke="url(#gGold)" stroke-width="2.2" stroke-linecap="round"/>
  <path d="M56 44 L58 45" stroke="url(#gGold)" stroke-width="1.6" stroke-linecap="round"/>
  
  <!-- Trunk with Modak -->
  <path d="M50 36 C52 44 48 53 52 62 C55 69 64 70 67 64 C69 58 63 56 60 58" fill="none" stroke="url(#gGold)" stroke-width="3.2" stroke-linecap="round"/>
  <circle cx="61" cy="57" r="3.2" fill="#E67E22"/>
  <circle cx="62" cy="56" r="1.2" fill="#F1C40F"/>
  
  <!-- Blessing Palm / Abhaya Mudra -->
  <path d="M33 50 C29 53 29 61 35 64 C38 65 42 61 41 57" fill="none" stroke="url(#gGold)" stroke-width="2.2" stroke-linecap="round"/>
  <circle cx="34" cy="57" r="1.3" fill="#C0392B"/>
</svg>
'''

MARIGOLD_TORAN_SVG = '''
<svg class="toran-svg" viewBox="0 0 1000 160" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="mgOrange" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FFA726"/>
      <stop offset="60%" stop-color="#E65100"/>
      <stop offset="100%" stop-color="#BF360C"/>
    </radialGradient>
    <radialGradient id="mgYellow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FFF59D"/>
      <stop offset="60%" stop-color="#FBC02D"/>
      <stop offset="100%" stop-color="#F57F17"/>
    </radialGradient>
    <linearGradient id="leafGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#388E3C"/>
      <stop offset="100%" stop-color="#1B5E20"/>
    </linearGradient>
    <linearGradient id="toranRibbon" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#C0392B"/>
      <stop offset="50%" stop-color="#D4AF37"/>
      <stop offset="100%" stop-color="#C0392B"/>
    </linearGradient>
  </defs>
  
  <!-- Top decorative band -->
  <rect x="0" y="0" width="1000" height="10" fill="url(#toranRibbon)"/>
  
  <!-- Mango Leaves Swag -->
  <path d="M 0 10 Q 70 30 140 10 Q 210 30 280 10 Q 350 30 420 10 Q 490 30 560 10 Q 630 30 700 10 Q 770 30 840 10 Q 910 30 1000 10" fill="none" stroke="url(#leafGrad)" stroke-width="4"/>
  
  <!-- Hanging strings (garlands) with swing class -->
  <!-- String 1 (x=70) -->
  <g class="garland-string" data-origin="70 10" style="transform-origin: 70px 10px;">
    <line x1="70" y1="10" x2="70" y2="110" stroke="#8D6E63" stroke-width="1.2" stroke-dasharray="2 2"/>
    <circle cx="70" cy="25" r="9" fill="url(#mgYellow)"/>
    <circle cx="70" cy="42" r="9" fill="url(#mgOrange)"/>
    <circle cx="70" cy="59" r="9" fill="url(#mgYellow)"/>
    <circle cx="70" cy="76" r="9" fill="url(#mgOrange)"/>
    <circle cx="70" cy="93" r="10" fill="url(#mgYellow)"/>
    <circle cx="70" cy="110" r="11" fill="url(#mgOrange)"/>
  </g>

  <!-- String 2 (x=210) -->
  <g class="garland-string" data-origin="210 10" style="transform-origin: 210px 10px;">
    <line x1="210" y1="10" x2="210" y2="140" stroke="#8D6E63" stroke-width="1.2" stroke-dasharray="2 2"/>
    <circle cx="210" cy="25" r="9" fill="url(#mgOrange)"/>
    <circle cx="210" cy="42" r="9" fill="url(#mgYellow)"/>
    <circle cx="210" cy="59" r="9" fill="url(#mgOrange)"/>
    <circle cx="210" cy="76" r="9" fill="url(#mgYellow)"/>
    <circle cx="210" cy="93" r="9" fill="url(#mgOrange)"/>
    <circle cx="210" cy="110" r="10" fill="url(#mgYellow)"/>
    <circle cx="210" cy="128" r="11" fill="url(#mgOrange)"/>
    <circle cx="210" cy="144" r="12" fill="url(#mgYellow)"/>
  </g>

  <!-- String 3 (x=350) -->
  <g class="garland-string" data-origin="350 10" style="transform-origin: 350px 10px;">
    <line x1="350" y1="10" x2="350" y2="115" stroke="#8D6E63" stroke-width="1.2" stroke-dasharray="2 2"/>
    <circle cx="350" cy="25" r="9" fill="url(#mgYellow)"/>
    <circle cx="350" cy="42" r="9" fill="url(#mgOrange)"/>
    <circle cx="350" cy="59" r="9" fill="url(#mgYellow)"/>
    <circle cx="350" cy="76" r="9" fill="url(#mgOrange)"/>
    <circle cx="350" cy="93" r="10" fill="url(#mgYellow)"/>
    <circle cx="350" cy="112" r="11" fill="url(#mgOrange)"/>
  </g>

  <!-- String 4 (x=500 - Centerpiece) -->
  <g class="garland-string" data-origin="500 10" style="transform-origin: 500px 10px;">
    <line x1="500" y1="10" x2="500" y2="155" stroke="#8D6E63" stroke-width="1.2" stroke-dasharray="2 2"/>
    <circle cx="500" cy="24" r="9" fill="url(#mgOrange)"/>
    <circle cx="500" cy="40" r="9" fill="url(#mgYellow)"/>
    <circle cx="500" cy="56" r="9" fill="url(#mgOrange)"/>
    <circle cx="500" cy="72" r="9" fill="url(#mgYellow)"/>
    <circle cx="500" cy="88" r="9" fill="url(#mgOrange)"/>
    <circle cx="500" cy="104" r="10" fill="url(#mgYellow)"/>
    <circle cx="500" cy="121" r="11" fill="url(#mgOrange)"/>
    <circle cx="500" cy="138" r="12" fill="url(#mgYellow)"/>
    <circle cx="500" cy="154" r="12.5" fill="url(#mgOrange)"/>
  </g>

  <!-- String 5 (x=650) -->
  <g class="garland-string" data-origin="650 10" style="transform-origin: 650px 10px;">
    <line x1="650" y1="10" x2="650" y2="115" stroke="#8D6E63" stroke-width="1.2" stroke-dasharray="2 2"/>
    <circle cx="650" cy="25" r="9" fill="url(#mgYellow)"/>
    <circle cx="650" cy="42" r="9" fill="url(#mgOrange)"/>
    <circle cx="650" cy="59" r="9" fill="url(#mgYellow)"/>
    <circle cx="650" cy="76" r="9" fill="url(#mgOrange)"/>
    <circle cx="650" cy="93" r="10" fill="url(#mgYellow)"/>
    <circle cx="650" cy="112" r="11" fill="url(#mgOrange)"/>
  </g>

  <!-- String 6 (x=790) -->
  <g class="garland-string" data-origin="790 10" style="transform-origin: 790px 10px;">
    <line x1="790" y1="10" x2="790" y2="140" stroke="#8D6E63" stroke-width="1.2" stroke-dasharray="2 2"/>
    <circle cx="790" cy="25" r="9" fill="url(#mgOrange)"/>
    <circle cx="790" cy="42" r="9" fill="url(#mgYellow)"/>
    <circle cx="790" cy="59" r="9" fill="url(#mgOrange)"/>
    <circle cx="790" cy="76" r="9" fill="url(#mgYellow)"/>
    <circle cx="790" cy="93" r="9" fill="url(#mgOrange)"/>
    <circle cx="790" cy="110" r="10" fill="url(#mgYellow)"/>
    <circle cx="790" cy="128" r="11" fill="url(#mgOrange)"/>
    <circle cx="790" cy="144" r="12" fill="url(#mgYellow)"/>
  </g>

  <!-- String 7 (x=930) -->
  <g class="garland-string" data-origin="930 10" style="transform-origin: 930px 10px;">
    <line x1="930" y1="10" x2="930" y2="110" stroke="#8D6E63" stroke-width="1.2" stroke-dasharray="2 2"/>
    <circle cx="930" cy="25" r="9" fill="url(#mgYellow)"/>
    <circle cx="930" cy="42" r="9" fill="url(#mgOrange)"/>
    <circle cx="930" cy="59" r="9" fill="url(#mgYellow)"/>
    <circle cx="930" cy="76" r="9" fill="url(#mgOrange)"/>
    <circle cx="930" cy="93" r="10" fill="url(#mgYellow)"/>
    <circle cx="930" cy="110" r="11" fill="url(#mgOrange)"/>
  </g>
</svg>
'''

CORNER_ROSE_SVG = '''
<svg class="corner-rose-svg" viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="roseWine" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#C0392B"/>
      <stop offset="60%" stop-color="#6E1F2F"/>
      <stop offset="100%" stop-color="#3A0D17"/>
    </radialGradient>
    <radialGradient id="roseBlush" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FADBD8"/>
      <stop offset="70%" stop-color="#E6B0AA"/>
      <stop offset="100%" stop-color="#D98880"/>
    </radialGradient>
    <linearGradient id="goldLeaf" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFEAA7"/>
      <stop offset="50%" stop-color="#D4AF37"/>
      <stop offset="100%" stop-color="#8C6510"/>
    </linearGradient>
  </defs>
  <!-- Golden Leaves -->
  <path d="M20 20 Q5 50 25 70 Q45 50 20 20 Z" fill="url(#goldLeaf)" opacity="0.85"/>
  <path d="M20 20 Q50 5 70 25 Q50 45 20 20 Z" fill="url(#goldLeaf)" opacity="0.85"/>
  <path d="M30 30 Q75 15 90 40 Q65 60 30 30 Z" fill="url(#goldLeaf)" opacity="0.75"/>
  
  <!-- Outer Wine Petals -->
  <path d="M45 45 C30 25 60 15 70 35 C80 20 100 40 85 55 C100 70 80 90 65 80 C50 95 30 75 40 60 C20 50 35 30 45 45 Z" fill="url(#roseWine)"/>
  
  <!-- Mid Petals -->
  <path d="M50 48 C42 38 62 32 68 44 C76 36 86 48 78 58 C86 68 72 78 62 72 C52 80 40 68 46 58 C36 52 44 40 50 48 Z" fill="#922B3E"/>
  
  <!-- Inner Rosette / Blush Highlights -->
  <circle cx="60" cy="55" r="16" fill="url(#roseWine)"/>
  <path d="M54 50 C58 46 64 46 66 50 C68 54 62 58 58 56 C54 54 52 52 54 50 Z" fill="url(#roseBlush)" opacity="0.85"/>
  <circle cx="60" cy="54" r="5" fill="#FFEAA7" opacity="0.9"/>
</svg>
'''

ARCH_TOP_SVG = '''
<svg class="arch-top-svg" viewBox="0 0 360 160" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="archGoldTop" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FFE082"/>
      <stop offset="30%" stop-color="#D4AF37"/>
      <stop offset="70%" stop-color="#AA771C"/>
      <stop offset="100%" stop-color="#FFE082"/>
    </linearGradient>
    <filter id="softGlowTop" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>
  
  <!-- Royal Arch Silhouette (Jharokha Cusps) -->
  <path d="M 24 160 
           L 24 105 
           C 24 60, 75 25, 135 25 
           C 155 25, 172 32, 180 40 
           C 188 32, 205 25, 225 25 
           C 285 25, 336 60, 336 105 
           L 336 160" 
        fill="none" stroke="url(#archGoldTop)" stroke-width="2.2" filter="url(#softGlowTop)"/>
        
  <!-- Top Finial / Kalash Motif -->
  <circle cx="180" cy="20" r="4.5" fill="url(#archGoldTop)"/>
  <path d="M 180 9 L 183.5 18 L 176.5 18 Z" fill="url(#archGoldTop)"/>
  
  <!-- Top Corner Rosettes -->
  <circle cx="24" cy="24" r="5" fill="none" stroke="url(#archGoldTop)" stroke-width="1.2"/>
  <circle cx="24" cy="24" r="2.2" fill="url(#archGoldTop)"/>
  
  <circle cx="336" cy="24" r="5" fill="none" stroke="url(#archGoldTop)" stroke-width="1.2"/>
  <circle cx="336" cy="24" r="2.2" fill="url(#archGoldTop)"/>
</svg>
'''

ARCH_BOTTOM_SVG = '''
<svg class="arch-bottom-svg" viewBox="0 0 360 40" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="archGoldBtm" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FFE082"/>
      <stop offset="50%" stop-color="#D4AF37"/>
      <stop offset="100%" stop-color="#FFE082"/>
    </linearGradient>
  </defs>
  <!-- Bottom Corner Rosettes -->
  <circle cx="24" cy="20" r="5" fill="none" stroke="url(#archGoldBtm)" stroke-width="1.2"/>
  <circle cx="24" cy="20" r="2.2" fill="url(#archGoldBtm)"/>
  
  <circle cx="336" cy="20" r="5" fill="none" stroke="url(#archGoldBtm)" stroke-width="1.2"/>
  <circle cx="336" cy="20" r="2.2" fill="url(#archGoldBtm)"/>
  
  <!-- Delicate Bottom Flourish Line -->
  <path d="M 40 20 L 140 20 M 220 20 L 320 20" stroke="url(#archGoldBtm)" stroke-width="0.8" stroke-dasharray="3 3"/>
  <circle cx="180" cy="20" r="2" fill="url(#archGoldBtm)"/>
</svg>
'''

# Festivities Scene SVGs

SCENE_LAKHDAV = '''
<svg viewBox="0 0 100 80" class="scene-illustration" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="brassGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFEAA7"/>
      <stop offset="50%" stop-color="#D4AF37"/>
      <stop offset="100%" stop-color="#996515"/>
    </linearGradient>
    <radialGradient id="diyaGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FFF9C4"/>
      <stop offset="60%" stop-color="#FF9800"/>
      <stop offset="100%" stop-color="#E65100" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <!-- Rangoli Base -->
  <ellipse cx="50" cy="70" rx="35" ry="7" fill="none" stroke="#D4AF37" stroke-width="1.2" stroke-dasharray="3 2"/>
  <ellipse cx="50" cy="70" rx="28" ry="5" fill="#FAF0E6" opacity="0.6"/>
  
  <!-- Kalash Pot (Brass) -->
  <path d="M38 46 Q34 65 50 67 Q66 65 62 46 Q58 43 50 43 Q42 43 38 46 Z" fill="url(#brassGrad)" stroke="#7A5210" stroke-width="0.8"/>
  <ellipse cx="50" cy="45" rx="12" ry="3" fill="#D4AF37" stroke="#7A5210" stroke-width="0.5"/>
  <!-- Sacred Swastika on Pot -->
  <path d="M48 51 L52 51 M50 49 L50 53 M48 49 L48 51 M52 51 L52 53 M48 53 L50 53 M50 49 L52 49" stroke="#C0392B" stroke-width="0.9" fill="none"/>
  
  <!-- Mango Leaves -->
  <path d="M42 43 Q32 32 30 22 Q40 30 46 41 Z" fill="#2E7D32"/>
  <path d="M58 43 Q68 32 70 22 Q60 30 54 41 Z" fill="#2E7D32"/>
  <path d="M50 42 Q40 25 43 14 Q48 26 50 40 Z" fill="#388E3C"/>
  <path d="M50 42 Q60 25 57 14 Q52 26 50 40 Z" fill="#388E3C"/>
  <path d="M50 42 Q50 18 50 10 Q52 25 50 40 Z" fill="#4CAF50"/>
  
  <!-- Coconut on Top -->
  <ellipse cx="50" cy="36" rx="9" ry="10" fill="#795548"/>
  <path d="M43 32 Q50 20 57 32 Z" fill="#5D4037"/>
  
  <!-- Small Diya next to Kalash -->
  <ellipse cx="76" cy="65" rx="9" ry="3.5" fill="url(#brassGrad)"/>
  <circle cx="76" cy="60" r="8" fill="url(#diyaGlow)"/>
  <path d="M76 63 Q74 57 76 53 Q78 57 76 63 Z" fill="#FFEB3B"/>
</svg>
'''

SCENE_TILAK = '''
<svg viewBox="0 0 100 80" class="scene-illustration" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="thaliGold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFF2A3"/>
      <stop offset="50%" stop-color="#D4AF37"/>
      <stop offset="100%" stop-color="#8C6510"/>
    </linearGradient>
  </defs>
  <!-- Thali Plate (3D tilt) -->
  <ellipse cx="50" cy="50" rx="42" ry="22" fill="url(#thaliGold)" stroke="#6E1F2F" stroke-width="1.5"/>
  <ellipse cx="50" cy="50" rx="38" ry="19" fill="#FFFDF9" stroke="#D4AF37" stroke-width="0.8"/>
  <ellipse cx="50" cy="50" rx="36" ry="17" fill="none" stroke="#C0392B" stroke-width="0.8" stroke-dasharray="2 2"/>
  
  <!-- Kumkum Bowl -->
  <ellipse cx="36" cy="46" rx="7" ry="4" fill="#A93226"/>
  <circle cx="36" cy="45" r="5" fill="#C0392B"/>
  
  <!-- Chandan Bowl -->
  <ellipse cx="48" cy="41" rx="6" ry="3.5" fill="#D4AF37"/>
  <circle cx="48" cy="40.5" r="4.5" fill="#F9E79F"/>
  
  <!-- Akshat (Rice pearls) -->
  <ellipse cx="60" cy="45" rx="7" ry="4" fill="#EAECEE"/>
  <circle cx="58" cy="44" r="1.2" fill="#FFFFFF"/>
  <circle cx="61" cy="45" r="1.2" fill="#FFFFFF"/>
  <circle cx="62" cy="43" r="1.2" fill="#FFFFFF"/>
  
  <!-- Brass Diya with Flame on Thali -->
  <ellipse cx="50" cy="57" rx="8" ry="4" fill="url(#thaliGold)"/>
  <circle cx="50" cy="52" r="7" fill="url(#diyaGlow)"/>
  <path d="M50 56 Q48 49 50 45 Q52 49 50 56 Z" fill="#FFF176"/>
  
  <!-- Betel Leaf (Paan Patta) -->
  <path d="M25 48 Q20 56 30 60 Q34 52 25 48 Z" fill="#2E7D32"/>
</svg>
'''

SCENE_HALDI = '''
<svg viewBox="0 0 100 80" class="scene-illustration" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="haldiPaste" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FFF176"/>
      <stop offset="60%" stop-color="#FBC02D"/>
      <stop offset="100%" stop-color="#F57F17"/>
    </radialGradient>
    <radialGradient id="marigoldYellow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FFF9C4"/>
      <stop offset="70%" stop-color="#FBC02D"/>
      <stop offset="100%" stop-color="#E65100"/>
    </radialGradient>
  </defs>
  <!-- Brass Urli Bowl -->
  <path d="M20 48 Q20 68 50 70 Q80 68 80 48 Q70 52 50 52 Q30 52 20 48 Z" fill="url(#brassGrad)" stroke="#7A5210" stroke-width="1.2"/>
  <ellipse cx="50" cy="48" rx="30" ry="8" fill="url(#haldiPaste)"/>
  <ellipse cx="50" cy="48" rx="27" ry="6.5" fill="#FBC02D" opacity="0.85"/>
  
  <!-- Floating Marigolds inside Urli -->
  <circle cx="38" cy="48" r="4.5" fill="url(#marigoldYellow)"/>
  <circle cx="62" cy="48" r="4.5" fill="url(#marigoldYellow)"/>
  <circle cx="50" cy="46" r="5" fill="url(#marigoldYellow)"/>
  
  <!-- Splashing Drops of Turmeric -->
  <circle cx="50" cy="28" r="2.5" fill="#FBC02D"/>
  <circle cx="43" cy="34" r="1.8" fill="#FDD835"/>
  <circle cx="58" cy="33" r="1.8" fill="#F57F17"/>
  <path d="M50 25 Q51 32 50 36" stroke="#FBC02D" stroke-width="1.5" stroke-linecap="round"/>
  
  <!-- Scattered Genda Phool on Ground -->
  <circle cx="16" cy="62" r="5" fill="url(#marigoldYellow)"/>
  <circle cx="84" cy="62" r="5" fill="url(#marigoldYellow)"/>
  <circle cx="26" cy="68" r="4" fill="url(#mgOrange)"/>
  <circle cx="74" cy="68" r="4" fill="url(#mgOrange)"/>
</svg>
'''

SCENE_MEHENDI = '''
<svg viewBox="0 0 100 80" class="scene-illustration" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="hennaGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4E342E"/>
      <stop offset="50%" stop-color="#6D4C41"/>
      <stop offset="100%" stop-color="#3E2723"/>
    </linearGradient>
  </defs>
  <!-- Beautiful Henna Hands Silhouette in Graceful Posture -->
  <!-- Left Hand -->
  <path d="M35 70 C33 55 35 45 32 38 C31 35 34 32 36 35 C38 40 37 46 39 40 C40 36 43 34 44 38 C45 42 43 47 45 42 C46 38 49 37 50 42 C51 47 47 55 45 68 Z" 
        fill="#FDF2E9" stroke="#6D4C41" stroke-width="1.2"/>
        
  <!-- Henna Mandala Pattern on Palm -->
  <circle cx="40" cy="55" r="6" fill="none" stroke="#5D4037" stroke-width="1.2"/>
  <circle cx="40" cy="55" r="3" fill="#6D4C41"/>
  <path d="M37 50 Q40 48 43 50 Q45 53 43 56 Q40 58 37 56 Q35 53 37 50 Z" fill="none" stroke="#6D4C41" stroke-width="0.8"/>
  
  <!-- Right Hand Gracefully Meeting -->
  <path d="M65 70 C67 55 65 45 68 38 C69 35 66 32 64 35 C62 40 63 46 61 40 C60 36 57 34 56 38 C55 42 57 47 55 42 C54 38 51 37 50 42 C49 47 53 55 55 68 Z" 
        fill="#FDF2E9" stroke="#6D4C41" stroke-width="1.2"/>
        
  <circle cx="60" cy="55" r="6" fill="none" stroke="#5D4037" stroke-width="1.2"/>
  <circle cx="60" cy="55" r="3" fill="#6D4C41"/>
  
  <!-- Green Henna Leaves / Paisley Flourishes around -->
  <path d="M18 35 Q24 25 32 30 Q28 40 18 35 Z" fill="#2E7D32" opacity="0.85"/>
  <path d="M82 35 Q76 25 68 30 Q72 40 82 35 Z" fill="#2E7D32" opacity="0.85"/>
  <circle cx="20" cy="45" r="2" fill="#D4AF37"/>
  <circle cx="80" cy="45" r="2" fill="#D4AF37"/>
</svg>
'''

SCENE_SANGEET = '''
<svg viewBox="0 0 100 80" class="scene-illustration" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="dholGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#8D6E63"/>
      <stop offset="50%" stop-color="#5D4037"/>
      <stop offset="100%" stop-color="#3E2723"/>
    </linearGradient>
  </defs>
  <!-- Celebratory Spotlight Glow -->
  <circle cx="50" cy="45" r="32" fill="#F8BBD0" opacity="0.35"/>
  <circle cx="50" cy="45" r="22" fill="#E1BEE7" opacity="0.4"/>
  
  <!-- Dhol Barrel -->
  <path d="M26 34 Q50 28 74 34 L72 58 Q50 64 28 58 Z" fill="url(#dholGrad)" stroke="#D4AF37" stroke-width="1.2"/>
  
  <!-- Dhol Heads / Membranes -->
  <ellipse cx="26" cy="46" rx="5" ry="12" fill="#FFF9C4" stroke="#D4AF37" stroke-width="1.2"/>
  <ellipse cx="73" cy="46" rx="5" ry="12" fill="#D7CCC8" stroke="#D4AF37" stroke-width="1.2"/>
  
  <!-- Dhol Ropes (Lacing) -->
  <path d="M28 35 L40 59 L52 33 L64 59 L73 35" fill="none" stroke="#FFECB3" stroke-width="1.2"/>
  <path d="M28 57 L40 33 L52 59 L64 33 L73 57" fill="none" stroke="#FFECB3" stroke-width="1.2"/>
  
  <!-- Dhol Sticks (Dagga & Tilli) -->
  <line x1="18" y1="28" x2="28" y2="44" stroke="#D4AF37" stroke-width="2.2" stroke-linecap="round"/>
  <line x1="82" y1="28" x2="72" y2="44" stroke="#D4AF37" stroke-width="1.6" stroke-linecap="round"/>
  
  <!-- Musical Notes & Sparkles Floating -->
  <path d="M38 18 L48 14 L48 24 M38 28 A3 3 0 1 1 38 22 A3 3 0 1 1 38 28 M48 24 A3 3 0 1 1 48 18 A3 3 0 1 1 48 24" 
        fill="#8E24AA" stroke="#8E24AA" stroke-width="1"/>
  <path d="M68 20 L68 12 L75 14" stroke="#E91E63" stroke-width="1.4" fill="none"/>
  <circle cx="68" cy="20" r="2.5" fill="#E91E63"/>
  
  <!-- Golden Sparkle Stars -->
  <path d="M20 22 L22 17 L24 22 L29 24 L24 26 L22 31 L20 26 L15 24 Z" fill="#D4AF37"/>
  <path d="M80 18 L81 14 L83 18 L87 19 L83 21 L81 25 L80 21 L76 19 Z" fill="#D4AF37"/>
</svg>
'''

SCENE_PHERAS = '''
<svg viewBox="0 0 100 80" class="scene-illustration" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="agniFire" cx="50%" cy="80%" r="70%">
      <stop offset="0%" stop-color="#FFF59D"/>
      <stop offset="40%" stop-color="#FF9800"/>
      <stop offset="80%" stop-color="#D32F2F"/>
      <stop offset="100%" stop-color="#B71C1C" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <!-- Royal Wedding Mandap Pillars -->
  <!-- Left Pillar -->
  <rect x="18" y="22" width="6" height="48" rx="2" fill="url(#brassGrad)"/>
  <path d="M15 22 L27 22 L24 18 L18 18 Z" fill="#D4AF37"/>
  <path d="M15 70 L27 70 L24 73 L18 73 Z" fill="#D4AF37"/>
  
  <!-- Right Pillar -->
  <rect x="76" y="22" width="6" height="48" rx="2" fill="url(#brassGrad)"/>
  <path d="M73 22 L85 22 L82 18 L76 18 Z" fill="#D4AF37"/>
  <path d="M73 70 L85 70 L82 73 L76 73 Z" fill="#D4AF37"/>
  
  <!-- Floral Arch Canopy (Toran style) -->
  <path d="M18 22 Q50 12 82 22" fill="none" stroke="#C0392B" stroke-width="2.5"/>
  <path d="M18 25 Q50 17 82 25" fill="none" stroke="#D4AF37" stroke-width="1.5"/>
  <circle cx="50" cy="18" r="4" fill="#FBC02D"/>
  
  <!-- Havan Kund (Sacred Altar) -->
  <path d="M36 68 L64 68 L60 56 L40 56 Z" fill="#A04000" stroke="#78281F" stroke-width="1.2"/>
  <rect x="34" y="68" width="32" height="3" fill="#D4AF37"/>
  
  <!-- Sacred Agni (Holy Fire Flames) -->
  <circle cx="50" cy="50" r="16" fill="url(#agniFire)"/>
  <path d="M50 36 Q45 46 48 56 Q52 48 50 36 Z" fill="#FFF9C4"/>
  <path d="M46 42 Q40 50 44 56 Q48 50 46 42 Z" fill="#FFC107"/>
  <path d="M54 42 Q60 50 56 56 Q52 50 54 42 Z" fill="#FF9800"/>
  
  <!-- Royal Shehnai in foreground -->
  <path d="M28 42 L16 32 Q14 30 12 33 Q14 36 18 36 L28 44 Z" fill="url(#brassGrad)" stroke="#5E400B" stroke-width="0.8"/>
  <ellipse cx="12" cy="32" rx="2.5" ry="4" fill="#D4AF37"/>
</svg>
'''

MAP_ROUTE_SVG = '''
<svg viewBox="0 0 320 140" class="map-route-svg" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="routeGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#C0392B"/>
      <stop offset="50%" stop-color="#D4AF37"/>
      <stop offset="100%" stop-color="#6E1F2F"/>
    </linearGradient>
  </defs>
  <!-- Background parchment map tile -->
  <rect x="4" y="4" width="312" height="132" rx="12" fill="#FAF6F0" stroke="#E2D7C8" stroke-width="1.2"/>
  
  <!-- Subtle terrain / river curve -->
  <path d="M 0 45 Q 80 80 160 50 T 320 60" fill="none" stroke="#E6EEF8" stroke-width="14" opacity="0.6"/>
  <path d="M 0 45 Q 80 80 160 50 T 320 60" fill="none" stroke="#D0E1F9" stroke-width="4" opacity="0.8"/>
  
  <!-- Route Line from Sahebganj (left) to Samastipur (right) -->
  <path id="weddingPath" d="M 50 85 Q 110 30 190 95 T 270 45" fill="none" stroke="url(#routeGrad)" stroke-width="3" stroke-dasharray="6 4" class="animated-route-line"/>
  
  <!-- Point A: Sahebganj (Residence) -->
  <g transform="translate(50, 85)">
    <circle cx="0" cy="0" r="10" fill="#FFEAA7" opacity="0.7" class="pulse-ring"/>
    <circle cx="0" cy="0" r="6" fill="#C0392B"/>
    <circle cx="0" cy="0" r="2.5" fill="#FFFFFF"/>
    <text x="0" y="20" font-family="'Montserrat', sans-serif" font-size="9" font-weight="600" fill="#6E1F2F" text-anchor="middle">Sahebganj</text>
    <text x="0" y="29" font-family="'Montserrat', sans-serif" font-size="7.5" fill="#888" text-anchor="middle">Residence</text>
  </g>
  
  <!-- Point B: Samastipur (Banquet Maa Jagdamba Palace) -->
  <g transform="translate(270, 45)">
    <circle cx="0" cy="0" r="12" fill="#FFD54F" opacity="0.6" class="pulse-ring"/>
    <circle cx="0" cy="0" r="7" fill="#6E1F2F"/>
    <circle cx="0" cy="0" r="3" fill="#D4AF37"/>
    <text x="0" y="21" font-family="'Montserrat', sans-serif" font-size="9" font-weight="700" fill="#6E1F2F" text-anchor="middle">Samastipur</text>
    <text x="0" y="30" font-family="'Montserrat', sans-serif" font-size="7.5" font-weight="600" fill="#D4AF37" text-anchor="middle">Banquet Palace</text>
  </g>
  
  <!-- Moving Royal Wedding Car along path -->
  <g id="movingCar">
    <animateMotion repeatCount="indefinite" dur="7s" path="M 50 85 Q 110 30 190 95 T 270 45" rotate="auto" />
    <circle cx="0" cy="0" r="9" fill="#FFFDF9" stroke="#D4AF37" stroke-width="1.5"/>
    <text x="0" y="3.5" font-size="10" text-anchor="middle">🚗</text>
  </g>
</svg>
'''

# Location SVGs for Singh's Residence and Delhi Reception

RESIDENCE_CARD_SVG = '''
<svg viewBox="0 0 320 130" class="map-route-svg" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="haveliGold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFEAA7"/>
      <stop offset="50%" stop-color="#D4AF37"/>
      <stop offset="100%" stop-color="#8C6510"/>
    </linearGradient>
    <radialGradient id="homeDiyaGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FFF9C4"/>
      <stop offset="60%" stop-color="#FF9800"/>
      <stop offset="100%" stop-color="#E65100" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <!-- Background parchment tile -->
  <rect x="4" y="4" width="312" height="122" rx="12" fill="#FAF6F0" stroke="#E2D7C8" stroke-width="1.2"/>
  
  <!-- Subtle decorative floral backdrop -->
  <circle cx="160" cy="55" r="42" fill="#FFFDF9" stroke="#EADBCC" stroke-width="0.8"/>
  
  <!-- Traditional Indian Home / Haveli Silhouette -->
  <!-- Roof / Chhatri -->
  <path d="M 120 40 Q 160 18 200 40 L 195 48 L 125 48 Z" fill="url(#haveliGold)"/>
  <circle cx="160" cy="18" r="3.5" fill="#C0392B"/>
  
  <!-- Doorway Arch -->
  <path d="M 135 48 L 135 98 L 185 98 L 185 48" fill="#FFFDF9" stroke="url(#haveliGold)" stroke-width="1.8"/>
  <path d="M 140 68 Q 160 48 180 68" fill="none" stroke="#C0392B" stroke-width="1.4"/>
  
  <!-- Hanging Marigold Toran over Entrance -->
  <path d="M 125 48 Q 142 56 160 48 Q 178 56 195 48" fill="none" stroke="#2E7D32" stroke-width="2"/>
  <circle cx="134" cy="53" r="3" fill="#FBC02D"/>
  <circle cx="143" cy="54" r="3" fill="#E65100"/>
  <circle cx="152" cy="53" r="3" fill="#FBC02D"/>
  <circle cx="168" cy="53" r="3" fill="#FBC02D"/>
  <circle cx="177" cy="54" r="3" fill="#E65100"/>
  <circle cx="186" cy="53" r="3" fill="#FBC02D"/>
  
  <!-- Two Pedestal Diyas -->
  <!-- Left Diya -->
  <rect x="95" y="75" width="10" height="23" rx="2" fill="url(#haveliGold)"/>
  <ellipse cx="100" cy="74" rx="7" ry="3" fill="#D4AF37"/>
  <circle cx="100" cy="69" r="6" fill="url(#homeDiyaGlow)"/>
  <path d="M100 72 Q98 67 100 64 Q102 67 100 72 Z" fill="#FFF176"/>
  
  <!-- Right Diya -->
  <rect x="215" y="75" width="10" height="23" rx="2" fill="url(#haveliGold)"/>
  <ellipse cx="220" cy="74" rx="7" ry="3" fill="#D4AF37"/>
  <circle cx="220" cy="69" r="6" fill="url(#homeDiyaGlow)"/>
  <path d="M220 72 Q218 67 220 64 Q222 67 220 72 Z" fill="#FFF176"/>
  
  <!-- Kalash inside doorway -->
  <ellipse cx="160" cy="92" rx="6" ry="4" fill="url(#haveliGold)"/>
  <circle cx="160" cy="86" r="3.5" fill="#795548"/>
  <path d="M156 86 Q160 81 164 86 Z" fill="#2E7D32"/>
  
  <!-- Rangoli Base -->
  <ellipse cx="160" cy="104" rx="38" ry="6" fill="none" stroke="#D4AF37" stroke-width="1" stroke-dasharray="2 2"/>
  
  <!-- Location Pin Tag -->
  <g transform="translate(48, 48)">
    <circle cx="0" cy="0" r="12" fill="#FFEAA7" opacity="0.6"/>
    <circle cx="0" cy="0" r="7" fill="#C0392B"/>
    <circle cx="0" cy="0" r="2.8" fill="#FFF"/>
  </g>
  <text x="50" y="72" font-family="'Montserrat', sans-serif" font-size="8.5" font-weight="700" fill="#6E1F2F" text-anchor="middle">Residence</text>
  <text x="50" y="82" font-family="'Montserrat', sans-serif" font-size="7.5" fill="#888" text-anchor="middle">Sahebganj</text>
  
  <!-- Auspicious Tag on right -->
  <g transform="translate(272, 48)">
    <circle cx="0" cy="0" r="12" fill="#FFF3CD" opacity="0.6"/>
    <circle cx="0" cy="0" r="7" fill="#D4AF37"/>
    <text x="0" y="2.5" font-size="7" text-anchor="middle">🏠</text>
  </g>
  <text x="272" y="72" font-family="'Montserrat', sans-serif" font-size="8.5" font-weight="700" fill="#6E1F2F" text-anchor="middle">Singh's</text>
  <text x="272" y="82" font-family="'Montserrat', sans-serif" font-size="7.5" fill="#888" text-anchor="middle">Family Home</text>
</svg>
'''

RECEPTION_CARD_SVG = '''
<svg viewBox="0 0 320 130" class="map-route-svg" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="delhiNightSky" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#2C0E1B"/>
      <stop offset="50%" stop-color="#4A1424"/>
      <stop offset="100%" stop-color="#6E1F2F"/>
    </linearGradient>
    <linearGradient id="monumentGold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFF3C4"/>
      <stop offset="50%" stop-color="#D4AF37"/>
      <stop offset="100%" stop-color="#8C6510"/>
    </linearGradient>
  </defs>
  <!-- Background night sky tile -->
  <rect x="4" y="4" width="312" height="122" rx="12" fill="url(#delhiNightSky)" stroke="#D4AF37" stroke-width="1.2"/>
  
  <!-- Twinkling stars -->
  <circle cx="35" cy="25" r="1.2" fill="#FFF"/>
  <circle cx="85" cy="18" r="1.5" fill="#FFEAA7"/>
  <circle cx="140" cy="15" r="1.2" fill="#FFF"/>
  <circle cx="230" cy="20" r="1.5" fill="#FFEAA7"/>
  <circle cx="280" cy="26" r="1.2" fill="#FFF"/>
  
  <!-- Celebratory golden sparkle bursts -->
  <path d="M55 35 L58 30 L61 35 L66 37 L61 39 L58 44 L55 39 L50 37 Z" fill="#D4AF37" opacity="0.8"/>
  <path d="M260 32 L262 28 L264 32 L268 34 L264 36 L262 40 L260 36 L256 34 Z" fill="#FFEAA7" opacity="0.85"/>
  
  <!-- Delhi Monument / India Gate & Royal Grand Banquet Silhouette -->
  <!-- Center India Gate Silhouette -->
  <path d="M 132 108 L 132 50 L 140 50 L 140 46 L 136 46 L 136 42 L 184 42 L 184 46 L 180 46 L 180 50 L 188 50 L 188 108 L 176 108 L 176 72 Q 160 62 144 72 L 144 108 Z" 
        fill="url(#monumentGold)" opacity="0.95"/>
  <rect x="144" y="48" width="32" height="3" fill="#FFEAA7"/>
  
  <!-- Grand Ballroom Pillars -->
  <!-- Left Ballroom Wing -->
  <rect x="75" y="65" width="4" height="43" fill="#D4AF37" opacity="0.6"/>
  <rect x="95" y="65" width="4" height="43" fill="#D4AF37" opacity="0.6"/>
  <path d="M 70 65 Q 100 55 125 65" stroke="#FFEAA7" stroke-width="1.2" fill="none" opacity="0.8"/>
  
  <!-- Right Ballroom Wing -->
  <rect x="221" y="65" width="4" height="43" fill="#D4AF37" opacity="0.6"/>
  <rect x="241" y="65" width="4" height="43" fill="#D4AF37" opacity="0.6"/>
  <path d="M 195 65 Q 220 55 250 65" stroke="#FFEAA7" stroke-width="1.2" fill="none" opacity="0.8"/>
  
  <!-- Royal Chandelier Light in Arch -->
  <circle cx="160" cy="65" r="4" fill="#FFF176"/>
  <line x1="160" y1="52" x2="160" y2="62" stroke="#FFEAA7" stroke-width="1"/>
  
  <!-- Location Pin Tag (New Delhi) -->
  <g transform="translate(42, 70)">
    <circle cx="0" cy="0" r="12" fill="#FFEAA7" opacity="0.4"/>
    <circle cx="0" cy="0" r="7" fill="#C0392B"/>
    <circle cx="0" cy="0" r="2.8" fill="#FFF"/>
  </g>
  <text x="42" y="94" font-family="'Montserrat', sans-serif" font-size="8" font-weight="700" fill="#FFEAA7" text-anchor="middle">Ghazipur</text>
  <text x="42" y="103" font-family="'Montserrat', sans-serif" font-size="7" fill="#E0C3C8" text-anchor="middle">New Delhi</text>
  
  <g transform="translate(278, 70)">
    <circle cx="0" cy="0" r="12" fill="#FFEAA7" opacity="0.4"/>
    <circle cx="0" cy="0" r="7" fill="#D4AF37"/>
    <text x="0" y="2.5" font-size="7" text-anchor="middle">✨</text>
  </g>
  <text x="278" y="94" font-family="'Montserrat', sans-serif" font-size="8" font-weight="700" fill="#FFEAA7" text-anchor="middle">Tarang</text>
  <text x="278" y="103" font-family="'Montserrat', sans-serif" font-size="7" fill="#E0C3C8" text-anchor="middle">Banquet Hall</text>
</svg>
'''
