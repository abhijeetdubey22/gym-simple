# -*- coding: utf-8 -*-
import re

with open('gym-standard-website.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add Hotspot CSS to <style>
hotspot_css = '''
    /* ==========================================================================
       INTERACTIVE EQUIPMENT HOTSPOTS & MOBILE CARDS
       ========================================================================== */
    .hotspot-wrapper {
      position: absolute;
      transform: translate(-50%, -50%);
      z-index: 25;
      cursor: pointer;
      -webkit-tap-highlight-color: transparent;
      user-select: none;
    }
    .hotspot-btn {
      width: 36px;
      height: 36px;
      border-radius: 50%;
      background: rgba(9, 11, 14, 0.92);
      border: 2px solid #f59e0b;
      color: #f59e0b;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 13px;
      box-shadow: 0 0 16px rgba(245, 158, 11, 0.65);
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      position: relative;
      z-index: 2;
    }
    .hotspot-ping-ring {
      position: absolute;
      inset: -6px;
      border-radius: 50%;
      background: #f59e0b;
      opacity: 0.5;
      animation: hotspotPingAnim 2.2s cubic-bezier(0, 0, 0.2, 1) infinite;
      pointer-events: none;
      z-index: 1;
    }
    @keyframes hotspotPingAnim {
      0% { transform: scale(0.8); opacity: 0.85; }
      100% { transform: scale(1.9); opacity: 0; }
    }
    .hotspot-wrapper:hover .hotspot-btn,
    .hotspot-wrapper.active .hotspot-btn {
      background: #f59e0b;
      color: #000000;
      transform: scale(1.15);
      box-shadow: 0 0 24px rgba(245, 158, 11, 0.95);
    }
    .hotspot-wrapper.active .hotspot-btn i {
      transform: rotate(45deg);
      transition: transform 0.2s ease;
    }

    /* Desktop Tooltip (Revealed on Hover or Active) */
    .hotspot-tooltip {
      position: absolute;
      bottom: calc(100% + 10px);
      left: 50%;
      transform: translateX(-50%) translateY(4px);
      background: rgba(9, 11, 14, 0.96);
      backdrop-filter: blur(14px);
      border: 1px solid rgba(245, 158, 11, 0.4);
      box-shadow: 0 12px 25px rgba(0, 0, 0, 0.9);
      border-radius: 10px;
      padding: 6px 12px;
      white-space: nowrap;
      pointer-events: none;
      opacity: 0;
      transition: all 0.2s ease-out;
      z-index: 30;
    }
    @media (min-width: 769px) {
      .hotspot-wrapper:hover .hotspot-tooltip,
      .hotspot-wrapper.active .hotspot-tooltip {
        opacity: 1;
        transform: translateX(-50%) translateY(0);
        pointer-events: auto;
      }
    }

    /* Floating Dock Card Inside Photo (Mobile Optimized) */
    .hotspot-dock-card {
      transition: opacity 0.25s ease, transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }
'''

if 'hotspotPingAnim' not in html:
    html = html.replace('</style>', hotspot_css + '\n  </style>')

# 2. Lower Floor Photo Hotspots & Card
lower_img_old = '''            <!-- Image Side -->
            <div class="lg:col-span-7 relative min-h-[280px] sm:min-h-[380px] bg-zinc-900">
              <img src="assets/lower_floor_hyrox_zumba.jpg" alt="Lower Floor HYROX, Cardio and Zumba" class="w-full h-full object-cover">
              <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent lg:bg-gradient-to-r lg:from-transparent lg:to-black/80"></div>
              <div class="absolute top-4 left-4 bg-black/80 backdrop-blur-md px-3 py-1.5 rounded-xl border border-amber-500/40 text-amber-300 text-xs font-bold uppercase tracking-wider flex items-center gap-1.5">
                <i class="fa-solid fa-layer-group text-amber-400"></i>
                <span>Lower Floor</span>
              </div>
            </div>'''

lower_img_new = '''            <!-- Image Side with Interactive Mobile Hotspots -->
            <div class="lg:col-span-7 relative min-h-[320px] sm:min-h-[420px] bg-zinc-900 overflow-hidden group/photo" id="lowerFloorPhotoContainer">
              <img src="assets/lower_floor_hyrox_zumba.jpg" alt="Lower Floor HYROX, Cardio and Zumba" class="w-full h-full object-cover">
              <div class="absolute inset-0 bg-gradient-to-t from-black/85 via-black/20 to-transparent lg:bg-gradient-to-r lg:from-transparent lg:to-black/80 pointer-events-none"></div>
              
              <!-- Badges -->
              <div class="absolute top-3.5 left-3.5 bg-black/85 backdrop-blur-md px-3 py-1.5 rounded-xl border border-amber-500/40 text-amber-300 text-xs font-bold uppercase tracking-wider flex items-center gap-1.5 z-10">
                <i class="fa-solid fa-layer-group text-amber-400"></i>
                <span>Lower Floor</span>
              </div>
              <div class="absolute top-3.5 right-3.5 bg-black/85 backdrop-blur-md px-2.5 py-1 rounded-xl border border-amber-500/30 text-amber-300 text-[11px] font-bold flex items-center gap-1.5 z-10 shadow-lg">
                <i class="fa-solid fa-hand-pointer text-amber-400 animate-pulse text-[10px]"></i>
                <span>Tap + to Inspect</span>
              </div>

              <!-- Interactive Hotspots -->
              <div class="hotspot-wrapper" style="top: 76%; left: 50%;"
                   data-title="HYROX Official 40M Turf Track"
                   data-category="Conditioning & Sled"
                   data-desc="Shock-absorbing competition turf engineered for heavy sled push/pull, walking lunges, and sprint intervals."
                   data-equip-id="sled_track">
                <div class="hotspot-ping-ring"></div>
                <button class="hotspot-btn" aria-label="Inspect HYROX Sled Track">
                  <i class="fa-solid fa-plus"></i>
                </button>
                <div class="hotspot-tooltip">
                  <div class="text-[10px] text-amber-400 font-bold uppercase">Conditioning & Sled</div>
                  <div class="font-bold text-white text-xs">HYROX Official 40M Turf Track</div>
                </div>
              </div>

              <div class="hotspot-wrapper" style="top: 54%; left: 16%;"
                   data-title="Motorless Curved Slat Treadmills"
                   data-category="Cardio Suite"
                   data-desc="Human-powered slatted curved belt demanding 30% more caloric burn with natural joint-cushioned stride."
                   data-equip-id="slat_treadmill">
                <div class="hotspot-ping-ring"></div>
                <button class="hotspot-btn" aria-label="Inspect Slat Treadmills">
                  <i class="fa-solid fa-plus"></i>
                </button>
                <div class="hotspot-tooltip">
                  <div class="text-[10px] text-amber-400 font-bold uppercase">Cardio Suite</div>
                  <div class="font-bold text-white text-xs">Motorless Curved Slat Treadmill</div>
                </div>
              </div>

              <div class="hotspot-wrapper" style="top: 40%; left: 86%;"
                   data-title="Zumba & Mind-Body Dance Studio"
                   data-category="Dance & Aerobics"
                   data-desc="Floating shock-absorbent hardwood dance floor with surrounding acoustic sound and ambient halo lighting."
                   data-equip-id="zumba_studio">
                <div class="hotspot-ping-ring"></div>
                <button class="hotspot-btn" aria-label="Inspect Zumba Studio">
                  <i class="fa-solid fa-plus"></i>
                </button>
                <div class="hotspot-tooltip">
                  <div class="text-[10px] text-amber-400 font-bold uppercase">Dance & Aerobics</div>
                  <div class="font-bold text-white text-xs">Zumba & Dance Studio</div>
                </div>
              </div>

              <div class="hotspot-wrapper" style="top: 48%; left: 36%;"
                   data-title="CrossFit & Functional Rig Zone"
                   data-category="Functional Training"
                   data-desc="Heavy structural steel rig for gymnastics rings, kipping pull-ups, wall ball targets, and rope climbs."
                   data-equip-id="power_rack">
                <div class="hotspot-ping-ring"></div>
                <button class="hotspot-btn" aria-label="Inspect Functional Rig">
                  <i class="fa-solid fa-plus"></i>
                </button>
                <div class="hotspot-tooltip">
                  <div class="text-[10px] text-amber-400 font-bold uppercase">Functional Training</div>
                  <div class="font-bold text-white text-xs">CrossFit & Functional Rig</div>
                </div>
              </div>

              <!-- Mobile Docked Equipment Info Card -->
              <div class="hotspot-dock-card absolute bottom-3 left-3 right-3 z-30 bg-black/95 backdrop-blur-xl border border-amber-500/40 rounded-2xl p-3 sm:p-3.5 shadow-2xl opacity-0 translate-y-3 pointer-events-none">
                <div class="flex items-start justify-between gap-2">
                  <div class="pr-2">
                    <span class="hotspot-card-category inline-block text-[10px] font-bold uppercase px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 mb-1">Equipment Specs</span>
                    <h4 class="hotspot-card-title font-bold text-white text-xs sm:text-sm">HYROX Official 40M Turf Track</h4>
                    <p class="hotspot-card-desc text-[11px] sm:text-xs text-zinc-300 mt-0.5 leading-snug">Shock-absorbing competition turf for heavy sled push/pull.</p>
                  </div>
                  <button class="hotspot-card-close w-7 h-7 rounded-full bg-zinc-800 hover:bg-zinc-700 text-zinc-400 hover:text-white flex items-center justify-center shrink-0 transition" aria-label="Close card">
                    <i class="fa-solid fa-xmark text-xs"></i>
                  </button>
                </div>
                <div class="mt-2.5 pt-2 border-t border-white/10 flex items-center justify-between">
                  <span class="text-[11px] text-amber-400 font-semibold flex items-center gap-1">
                    <i class="fa-solid fa-bolt text-[10px]"></i> Floor Blueprint
                  </span>
                  <button class="hotspot-card-action text-xs font-bold text-black bg-amber-500 hover:bg-amber-400 px-3 py-1.5 rounded-lg flex items-center gap-1.5 shadow-md active:scale-95 transition">
                    <span>Inspect Specs</span>
                    <i class="fa-solid fa-arrow-right text-[10px]"></i>
                  </button>
                </div>
              </div>
            </div>'''

html = html.replace(lower_img_old, lower_img_new)

# 3. Upper Floor Photo Hotspots & Card
upper_img_old = '''            <!-- Image Side -->
            <div class="lg:col-span-7 relative min-h-[280px] sm:min-h-[380px] bg-zinc-900 order-1 lg:order-2">
              <img src="assets/upper_floor_strength.jpg" alt="Upper Floor Heavy Strength and Weights" class="w-full h-full object-cover">
              <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent lg:bg-gradient-to-l lg:from-transparent lg:to-black/80"></div>
              <div class="absolute top-4 right-4 bg-black/80 backdrop-blur-md px-3 py-1.5 rounded-xl border border-amber-500/40 text-amber-300 text-xs font-bold uppercase tracking-wider flex items-center gap-1.5">
                <i class="fa-solid fa-dumbbell text-amber-400"></i>
                <span>Upper Floor</span>
              </div>
            </div>'''

upper_img_new = '''            <!-- Image Side with Interactive Mobile Hotspots -->
            <div class="lg:col-span-7 relative min-h-[320px] sm:min-h-[420px] bg-zinc-900 order-1 lg:order-2 overflow-hidden group/photo" id="upperFloorPhotoContainer">
              <img src="assets/upper_floor_strength.jpg" alt="Upper Floor Heavy Strength and Weights" class="w-full h-full object-cover">
              <div class="absolute inset-0 bg-gradient-to-t from-black/85 via-black/20 to-transparent lg:bg-gradient-to-l lg:from-transparent lg:to-black/80 pointer-events-none"></div>
              
              <!-- Badges -->
              <div class="absolute top-3.5 left-3.5 bg-black/85 backdrop-blur-md px-3 py-1.5 rounded-xl border border-amber-500/40 text-amber-300 text-xs font-bold uppercase tracking-wider flex items-center gap-1.5 z-10">
                <i class="fa-solid fa-dumbbell text-amber-400"></i>
                <span>Upper Floor</span>
              </div>
              <div class="absolute top-3.5 right-3.5 bg-black/85 backdrop-blur-md px-2.5 py-1 rounded-xl border border-amber-500/30 text-amber-300 text-[11px] font-bold flex items-center gap-1.5 z-10 shadow-lg">
                <i class="fa-solid fa-hand-pointer text-amber-400 animate-pulse text-[10px]"></i>
                <span>Tap + to Inspect</span>
              </div>

              <!-- Interactive Hotspots -->
              <div class="hotspot-wrapper" style="top: 68%; left: 15%;"
                   data-title="Plate-Loaded Leg Curl & Extension"
                   data-category="Legs & Hamstrings"
                   data-desc="Isolateral pivoting plate-loaded dual units delivering continuous tension without knee shearing stress."
                   data-equip-id="hack_squat">
                <div class="hotspot-ping-ring"></div>
                <button class="hotspot-btn" aria-label="Inspect Leg Curl Machine">
                  <i class="fa-solid fa-plus"></i>
                </button>
                <div class="hotspot-tooltip">
                  <div class="text-[10px] text-amber-400 font-bold uppercase">Legs & Hamstrings</div>
                  <div class="font-bold text-white text-xs">Plate-Loaded Leg Curl & Extension</div>
                </div>
              </div>

              <div class="hotspot-wrapper" style="top: 60%; left: 86%;"
                   data-title="Iso-Lateral Incline Chest Press"
                   data-category="Chest & Arms"
                   data-desc="Independent converging arms mimicking optimal dumbbell trajectory for maximum clavicular chest hypertrophy."
                   data-equip-id="incline_press">
                <div class="hotspot-ping-ring"></div>
                <button class="hotspot-btn" aria-label="Inspect Incline Chest Press">
                  <i class="fa-solid fa-plus"></i>
                </button>
                <div class="hotspot-tooltip">
                  <div class="text-[10px] text-amber-400 font-bold uppercase">Chest & Arms</div>
                  <div class="font-bold text-white text-xs">Iso-Lateral Incline Chest Press</div>
                </div>
              </div>

              <div class="hotspot-wrapper" style="top: 48%; left: 60%;"
                   data-title="8-Stack Multi-Jungle Cable Suite"
                   data-category="Cables & Functional"
                   data-desc="Aircraft-grade steel cables, dual adjustable swivel pulleys, lat pulldowns, and tricep pushdown stations."
                   data-equip-id="cable_crossover">
                <div class="hotspot-ping-ring"></div>
                <button class="hotspot-btn" aria-label="Inspect Cable Suite">
                  <i class="fa-solid fa-plus"></i>
                </button>
                <div class="hotspot-tooltip">
                  <div class="text-[10px] text-amber-400 font-bold uppercase">Cables & Functional</div>
                  <div class="font-bold text-white text-xs">8-Stack Multi-Jungle Cable Suite</div>
                </div>
              </div>

              <div class="hotspot-wrapper" style="top: 50%; left: 22%;"
                   data-title="Heavy Pro Dumbbell Racks (Up to 50KG)"
                   data-category="Free Weights"
                   data-desc="Solid urethane encased dumbbells ranging from 2KG up to 50KG on heavy vibration-absorbing rubberized steel racks."
                   data-equip-id="dumbbells">
                <div class="hotspot-ping-ring"></div>
                <button class="hotspot-btn" aria-label="Inspect Dumbbell Arsenal">
                  <i class="fa-solid fa-plus"></i>
                </button>
                <div class="hotspot-tooltip">
                  <div class="text-[10px] text-amber-400 font-bold uppercase">Free Weights</div>
                  <div class="font-bold text-white text-xs">Pro Dumbbells Up to 50KG</div>
                </div>
              </div>

              <!-- Mobile Docked Equipment Info Card -->
              <div class="hotspot-dock-card absolute bottom-3 left-3 right-3 z-30 bg-black/95 backdrop-blur-xl border border-amber-500/40 rounded-2xl p-3 sm:p-3.5 shadow-2xl opacity-0 translate-y-3 pointer-events-none">
                <div class="flex items-start justify-between gap-2">
                  <div class="pr-2">
                    <span class="hotspot-card-category inline-block text-[10px] font-bold uppercase px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 mb-1">Equipment Specs</span>
                    <h4 class="hotspot-card-title font-bold text-white text-xs sm:text-sm">Iso-Lateral Incline Chest Press</h4>
                    <p class="hotspot-card-desc text-[11px] sm:text-xs text-zinc-300 mt-0.5 leading-snug">Independent converging arms with 350KG capacity.</p>
                  </div>
                  <button class="hotspot-card-close w-7 h-7 rounded-full bg-zinc-800 hover:bg-zinc-700 text-zinc-400 hover:text-white flex items-center justify-center shrink-0 transition" aria-label="Close card">
                    <i class="fa-solid fa-xmark text-xs"></i>
                  </button>
                </div>
                <div class="mt-2.5 pt-2 border-t border-white/10 flex items-center justify-between">
                  <span class="text-[11px] text-amber-400 font-semibold flex items-center gap-1">
                    <i class="fa-solid fa-bolt text-[10px]"></i> Floor Blueprint
                  </span>
                  <button class="hotspot-card-action text-xs font-bold text-black bg-amber-500 hover:bg-amber-400 px-3 py-1.5 rounded-lg flex items-center gap-1.5 shadow-md active:scale-95 transition">
                    <span>Inspect Specs</span>
                    <i class="fa-solid fa-arrow-right text-[10px]"></i>
                  </button>
                </div>
              </div>
            </div>'''

html = html.replace(upper_img_old, upper_img_new)

# 4. Add Skyline Rooftop Arena & Interactive Visualizer directly above Equipment section
skyline_section_html = '''
    <!-- INTERACTIVE FLOOR & SKYLINE HARDWARE VISUALIZER -->
    <section class="py-12 bg-black border-b border-white/5" id="interactive-visualizer">
      <div class="max-w-6xl mx-auto px-4">
        
        <div class="text-center sm:text-left mb-6 flex flex-col sm:flex-row sm:items-end justify-between gap-4">
          <div>
            <span class="text-amber-500 text-[11px] font-bold uppercase tracking-wider flex items-center justify-center sm:justify-start gap-1.5">
              <i class="fa-solid fa-crosshairs text-amber-400"></i> Interactive Floor Blueprint
            </span>
            <h2 class="heading-font text-2xl sm:text-3xl font-bold text-white mt-1">Explore Hardware On-Floor</h2>
            <p class="text-xs text-zinc-400 mt-1">Tap any glowing + hotspot on the photo to reveal commercial specifications.</p>
          </div>
          
          <!-- View Switch Tabs -->
          <div class="flex items-center gap-1.5 bg-zinc-900/90 p-1.5 rounded-2xl border border-white/10 self-center sm:self-auto overflow-x-auto no-scrollbar max-w-full" id="visualizerTabs">
            <button class="vis-tab-btn active px-3 py-1.5 rounded-xl text-xs font-bold bg-amber-500 text-black shadow-md transition" data-view="skyline">
              <i class="fa-solid fa-sun text-[10px]"></i> Skyline Rooftop
            </button>
            <button class="vis-tab-btn px-3 py-1.5 rounded-xl text-xs font-bold text-zinc-300 hover:text-white transition" data-view="lower">
              <i class="fa-solid fa-layer-group text-[10px]"></i> Lower Floor
            </button>
            <button class="vis-tab-btn px-3 py-1.5 rounded-xl text-xs font-bold text-zinc-300 hover:text-white transition" data-view="upper">
              <i class="fa-solid fa-dumbbell text-[10px]"></i> Upper Floor
            </button>
          </div>
        </div>

        <!-- Visualizer Frame Container -->
        <div class="glass-card rounded-3xl overflow-hidden border border-white/10 relative min-h-[340px] sm:min-h-[460px] bg-zinc-950 group/vis" id="mainVisualizerContainer">
          
          <!-- View 1: Skyline Rooftop Arena (Matching User Screenshot) -->
          <div class="vis-pane active absolute inset-0 transition-opacity duration-300" id="pane-skyline">
            <img src="assets/outdoor_gym.jpg" alt="Skyline Rooftop Arena" class="w-full h-full object-cover">
            <div class="absolute inset-0 bg-gradient-to-t from-black/85 via-transparent to-black/30 pointer-events-none"></div>
            
            <div class="absolute top-4 left-4 bg-black/85 backdrop-blur-md px-3 py-1.5 rounded-xl border border-amber-500/40 text-amber-300 text-xs font-bold uppercase tracking-wider flex items-center gap-1.5 z-10">
              <i class="fa-solid fa-sun text-amber-400"></i>
              <span>Skyline Rooftop Arena</span>
            </div>
            <div class="absolute top-4 right-4 bg-black/85 backdrop-blur-md px-2.5 py-1 rounded-xl border border-amber-500/30 text-amber-300 text-[11px] font-bold flex items-center gap-1.5 z-10 shadow-lg">
              <i class="fa-solid fa-hand-pointer text-amber-400 animate-pulse text-[10px]"></i>
              <span>Tap + for Info</span>
            </div>

            <!-- Skyline Hotspots (Exact matches to user screenshot) -->
            <div class="hotspot-wrapper" style="top: 45%; left: 75%;"
                 data-title="Custom Rig with Flying Monkey Bars & Rings"
                 data-category="Calisthenics & Rigs"
                 data-desc="Heavy-duty outdoor calisthenics rig featuring multi-level pull up bars, flying monkey bars, and Olympic gymnastics rings."
                 data-equip-id="calisthenics_rig">
              <div class="hotspot-ping-ring"></div>
              <button class="hotspot-btn" aria-label="Inspect Custom Rig">
                <i class="fa-solid fa-plus"></i>
              </button>
              <div class="hotspot-tooltip">
                <div class="text-[10px] text-amber-400 font-bold uppercase">Calisthenics & Rigs</div>
                <div class="font-bold text-white text-xs">Custom Rig with Flying Monkey Bars & Rings</div>
              </div>
            </div>

            <div class="hotspot-wrapper" style="top: 65%; left: 12%;"
                 data-title="All-Weather Rubber Coated Dumbbell Racks"
                 data-category="Free Weights"
                 data-desc="Commercial all-weather rubber hex dumbbells from 2.5KG to 40KG on heavy dual-tier angled steel racks."
                 data-equip-id="outdoor_dumbbells">
              <div class="hotspot-ping-ring"></div>
              <button class="hotspot-btn" aria-label="Inspect Outdoor Dumbbells">
                <i class="fa-solid fa-plus"></i>
              </button>
              <div class="hotspot-tooltip">
                <div class="text-[10px] text-amber-400 font-bold uppercase">Free Weights</div>
                <div class="font-bold text-white text-xs">All-Weather Rubber Coated Dumbbell Racks</div>
              </div>
            </div>

            <div class="hotspot-wrapper" style="top: 55%; left: 50%;"
                 data-title="Heavy Battle Ropes & Sled Prowler Track"
                 data-category="Conditioning Track"
                 data-desc="50-foot 50mm poly-dacron battle ropes combined with dual-handle prowler sled on outdoor sprint turf."
                 data-equip-id="battle_ropes">
              <div class="hotspot-ping-ring"></div>
              <button class="hotspot-btn" aria-label="Inspect Battle Ropes Track">
                <i class="fa-solid fa-plus"></i>
              </button>
              <div class="hotspot-tooltip">
                <div class="text-[10px] text-amber-400 font-bold uppercase">Conditioning Track</div>
                <div class="font-bold text-white text-xs">Heavy Battle Ropes & Sled Prowler Track</div>
              </div>
            </div>
          </div>

          <!-- View 2: Lower Floor View -->
          <div class="vis-pane hidden opacity-0 absolute inset-0 transition-opacity duration-300" id="pane-lower">
            <img src="assets/lower_floor_hyrox_zumba.jpg" alt="Lower Floor HYROX and Zumba" class="w-full h-full object-cover">
            <div class="absolute inset-0 bg-gradient-to-t from-black/85 via-transparent to-black/30 pointer-events-none"></div>
            
            <div class="absolute top-4 left-4 bg-black/85 backdrop-blur-md px-3 py-1.5 rounded-xl border border-amber-500/40 text-amber-300 text-xs font-bold uppercase tracking-wider flex items-center gap-1.5 z-10">
              <i class="fa-solid fa-layer-group text-amber-400"></i>
              <span>Lower Floor: HYROX & Conditioning</span>
            </div>

            <div class="hotspot-wrapper" style="top: 76%; left: 50%;"
                 data-title="HYROX Official 40M Turf Track"
                 data-category="Conditioning & Sled"
                 data-desc="Official competition turf for heavy sled push/pull, walking lunges, and sprint intervals."
                 data-equip-id="sled_track">
              <div class="hotspot-ping-ring"></div>
              <button class="hotspot-btn"><i class="fa-solid fa-plus"></i></button>
              <div class="hotspot-tooltip">
                <div class="text-[10px] text-amber-400 font-bold uppercase">Conditioning & Sled</div>
                <div class="font-bold text-white text-xs">HYROX Official 40M Turf Track</div>
              </div>
            </div>

            <div class="hotspot-wrapper" style="top: 54%; left: 16%;"
                 data-title="Motorless Curved Slat Treadmills"
                 data-category="Cardio Suite"
                 data-desc="Human-powered slatted curved belt demanding 30% more caloric burn with natural joint-cushioned stride."
                 data-equip-id="slat_treadmill">
              <div class="hotspot-ping-ring"></div>
              <button class="hotspot-btn"><i class="fa-solid fa-plus"></i></button>
              <div class="hotspot-tooltip">
                <div class="text-[10px] text-amber-400 font-bold uppercase">Cardio Suite</div>
                <div class="font-bold text-white text-xs">Motorless Curved Slat Treadmill</div>
              </div>
            </div>

            <div class="hotspot-wrapper" style="top: 40%; left: 86%;"
                 data-title="Zumba & Mind-Body Dance Studio"
                 data-category="Dance & Aerobics"
                 data-desc="Floating hardwood dance floor with surrounding acoustic sound and ambient halo lighting."
                 data-equip-id="zumba_studio">
              <div class="hotspot-ping-ring"></div>
              <button class="hotspot-btn"><i class="fa-solid fa-plus"></i></button>
              <div class="hotspot-tooltip">
                <div class="text-[10px] text-amber-400 font-bold uppercase">Dance & Aerobics</div>
                <div class="font-bold text-white text-xs">Zumba & Dance Studio</div>
              </div>
            </div>
          </div>

          <!-- View 3: Upper Floor View -->
          <div class="vis-pane hidden opacity-0 absolute inset-0 transition-opacity duration-300" id="pane-upper">
            <img src="assets/upper_floor_strength.jpg" alt="Upper Floor Heavy Strength" class="w-full h-full object-cover">
            <div class="absolute inset-0 bg-gradient-to-t from-black/85 via-transparent to-black/30 pointer-events-none"></div>
            
            <div class="absolute top-4 left-4 bg-black/85 backdrop-blur-md px-3 py-1.5 rounded-xl border border-amber-500/40 text-amber-300 text-xs font-bold uppercase tracking-wider flex items-center gap-1.5 z-10">
              <i class="fa-solid fa-dumbbell text-amber-400"></i>
              <span>Upper Floor: Strength & Iron</span>
            </div>

            <div class="hotspot-wrapper" style="top: 68%; left: 15%;"
                 data-title="Plate-Loaded Leg Curl & Extension"
                 data-category="Legs & Hamstrings"
                 data-desc="Isolateral pivoting plate-loaded dual units delivering continuous tension without knee shearing stress."
                 data-equip-id="hack_squat">
              <div class="hotspot-ping-ring"></div>
              <button class="hotspot-btn"><i class="fa-solid fa-plus"></i></button>
              <div class="hotspot-tooltip">
                <div class="text-[10px] text-amber-400 font-bold uppercase">Legs & Hamstrings</div>
                <div class="font-bold text-white text-xs">Plate-Loaded Leg Curl & Extension</div>
              </div>
            </div>

            <div class="hotspot-wrapper" style="top: 60%; left: 86%;"
                 data-title="Iso-Lateral Incline Chest Press"
                 data-category="Chest & Arms"
                 data-desc="Independent converging arms mimicking optimal dumbbell trajectory for maximum clavicular chest hypertrophy."
                 data-equip-id="incline_press">
              <div class="hotspot-ping-ring"></div>
              <button class="hotspot-btn"><i class="fa-solid fa-plus"></i></button>
              <div class="hotspot-tooltip">
                <div class="text-[10px] text-amber-400 font-bold uppercase">Chest & Arms</div>
                <div class="font-bold text-white text-xs">Iso-Lateral Incline Chest Press</div>
              </div>
            </div>

            <div class="hotspot-wrapper" style="top: 48%; left: 60%;"
                 data-title="8-Stack Multi-Jungle Cable Suite"
                 data-category="Cables & Functional"
                 data-desc="Aircraft-grade steel cables, dual adjustable swivel pulleys, lat pulldowns, and tricep pushdown stations."
                 data-equip-id="cable_crossover">
              <div class="hotspot-ping-ring"></div>
              <button class="hotspot-btn"><i class="fa-solid fa-plus"></i></button>
              <div class="hotspot-tooltip">
                <div class="text-[10px] text-amber-400 font-bold uppercase">Cables & Functional</div>
                <div class="font-bold text-white text-xs">8-Stack Multi-Jungle Cable Suite</div>
              </div>
            </div>
          </div>

          <!-- Shared Mobile Docked Equipment Info Card -->
          <div class="hotspot-dock-card absolute bottom-3 left-3 right-3 z-30 bg-black/95 backdrop-blur-xl border border-amber-500/40 rounded-2xl p-3.5 shadow-2xl opacity-0 translate-y-3 pointer-events-none">
            <div class="flex items-start justify-between gap-2">
              <div class="pr-2">
                <span class="hotspot-card-category inline-block text-[10px] font-bold uppercase px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 mb-1">Equipment Specs</span>
                <h4 class="hotspot-card-title font-bold text-white text-xs sm:text-sm">Tap any + hotspot to inspect</h4>
                <p class="hotspot-card-desc text-[11px] sm:text-xs text-zinc-300 mt-0.5 leading-snug">Explore commercial hardware across this floor.</p>
              </div>
              <button class="hotspot-card-close w-7 h-7 rounded-full bg-zinc-800 hover:bg-zinc-700 text-zinc-400 hover:text-white flex items-center justify-center shrink-0 transition" aria-label="Close card">
                <i class="fa-solid fa-xmark text-xs"></i>
              </button>
            </div>
            <div class="mt-2.5 pt-2 border-t border-white/10 flex items-center justify-between">
              <span class="text-[11px] text-amber-400 font-semibold flex items-center gap-1">
                <i class="fa-solid fa-bolt text-[10px]"></i> Floor Blueprint
              </span>
              <button class="hotspot-card-action text-xs font-bold text-black bg-amber-500 hover:bg-amber-400 px-3 py-1.5 rounded-lg flex items-center gap-1.5 shadow-md active:scale-95 transition">
                <span>Inspect Specs</span>
                <i class="fa-solid fa-arrow-right text-[10px]"></i>
              </button>
            </div>
          </div>

        </div>

      </div>
    </section>
'''

if 'id="interactive-visualizer"' not in html:
    html = html.replace('<!-- EQUIPMENT ARSENAL (INTERACTIVE WITH MODAL) -->', skyline_section_html + '\n    <!-- EQUIPMENT ARSENAL (INTERACTIVE WITH MODAL) -->')

# 5. Extend equipData with all hotspot items
equip_data_additions = '''
      sled_track: {
        title: "HYROX Official 40M Turf Track",
        category: "Conditioning & Sled",
        img: "assets/lower_floor_hyrox_zumba.jpg",
        desc: "Official competition shock-absorbing sprint and sled turf track engineered for heavy push/pull sleds, lunges, and interval conditioning.",
        target: "Full Body Conditioning, Hamstrings & Cardio Output",
        capacity: "Unlimited Heavy Sled Resistance",
        bestFor: "Official HYROX Training & Functional Anaerobic Power"
      },
      zumba_studio: {
        title: "Zumba & Mind-Body Dance Studio",
        category: "Dance & Aerobics",
        img: "assets/lower_floor_hyrox_zumba.jpg",
        desc: "High-energy group studio featuring floating sprung hardwood flooring for knee and ankle joint protection with concert acoustics.",
        target: "Cardiovascular Stamina, Rhythm & Full Body Coordination",
        capacity: "45+ Members Group Studio",
        bestFor: "High-Calorie Fat Burning & Energy Dance Fitness"
      },
      calisthenics_rig: {
        title: "Custom Rig with Flying Monkey Bars & Rings",
        category: "Calisthenics & Rigs",
        img: "assets/outdoor_gym.jpg",
        desc: "Commercial structural steel rig featuring flying monkey bars, Olympic gymnastics rings, parallel dip bars, and multi-grip pull-up stations.",
        target: "Lats, Upper Body Pull/Push, Core & Grip Strength",
        capacity: "Heavy Gauge Weather-Treated Structural Steel",
        bestFor: "Street Workout, Muscle-Ups & Functional Bodyweight Mastery"
      },
      outdoor_dumbbells: {
        title: "All-Weather Rubber Coated Dumbbell Racks",
        category: "Free Weights",
        img: "assets/outdoor_gym.jpg",
        desc: "Commercial weather-sealed rubber hex dumbbells ranging from 2.5KG to 40KG mounted on heavy dual-tier angled steel racks.",
        target: "Full Body Hypertrophy & Unilateral Symmetry",
        capacity: "Up to 40 KG per Dumbbell",
        bestFor: "Open-Air Hypertrophy Training with City Skyline Views"
      },
      battle_ropes: {
        title: "Heavy Battle Ropes & Sled Prowler Track",
        category: "Conditioning Track",
        img: "assets/outdoor_gym.jpg",
        desc: "50-foot 50mm heavy poly-dacron battle ropes combined with dual-handle prowler sled on outdoor sprint turf track.",
        target: "Shoulders, Arms, Core & Anaerobic Lactate Threshold",
        capacity: "50mm Heavy Gauge Poly-Dacron",
        bestFor: "Explosive Upper Body Conditioning & High-Intensity Intervals"
      },
'''

if 'calisthenics_rig' not in html:
    html = html.replace('const equipData = {', 'const equipData = {' + equip_data_additions)

# 6. Add JavaScript for Hotspots Interaction
hotspot_js = '''
    // ==========================================================================
    // INTERACTIVE HOTSPOTS ENGINE (MOBILE & DESKTOP)
    // ==========================================================================
    function initHotspots() {
      // Setup each container with its hotspots and dock card
      const containers = document.querySelectorAll('#lowerFloorPhotoContainer, #upperFloorPhotoContainer, #mainVisualizerContainer');
      
      containers.forEach(container => {
        const hotspots = container.querySelectorAll('.hotspot-wrapper');
        const dockCard = container.querySelector('.hotspot-dock-card');
        if (!dockCard) return;

        const cardCategory = dockCard.querySelector('.hotspot-card-category');
        const cardTitle = dockCard.querySelector('.hotspot-card-title');
        const cardDesc = dockCard.querySelector('.hotspot-card-desc');
        const cardAction = dockCard.querySelector('.hotspot-card-action');
        const cardClose = dockCard.querySelector('.hotspot-card-close');

        function openCardForHotspot(spot) {
          const title = spot.dataset.title;
          const category = spot.dataset.category;
          const desc = spot.dataset.desc;
          const equipId = spot.dataset.equipId;

          if (cardCategory) cardCategory.textContent = category;
          if (cardTitle) cardTitle.textContent = title;
          if (cardDesc) cardDesc.textContent = desc;
          if (cardAction) cardAction.dataset.equipId = equipId;

          // Highlight active hotspot
          hotspots.forEach(h => h.classList.remove('active'));
          spot.classList.add('active');

          // Reveal dock card smoothly
          dockCard.classList.remove('opacity-0', 'translate-y-3', 'pointer-events-none');
          dockCard.classList.add('opacity-100', 'translate-y-0', 'pointer-events-auto');
        }

        function closeCard() {
          hotspots.forEach(h => h.classList.remove('active'));
          dockCard.classList.remove('opacity-100', 'translate-y-0', 'pointer-events-auto');
          dockCard.classList.add('opacity-0', 'translate-y-3', 'pointer-events-none');
        }

        hotspots.forEach(spot => {
          spot.addEventListener('click', (e) => {
            e.stopPropagation();
            if (spot.classList.contains('active')) {
              closeCard();
            } else {
              openCardForHotspot(spot);
            }
          });
        });

        if (cardClose) {
          cardClose.addEventListener('click', (e) => {
            e.stopPropagation();
            closeCard();
          });
        }

        if (cardAction) {
          cardAction.addEventListener('click', (e) => {
            e.stopPropagation();
            const equipId = cardAction.dataset.equipId;
            if (equipId && typeof openEquipmentById === 'function') {
              openEquipmentById(equipId);
            }
          });
        }

        // Tap outside to dismiss
        document.addEventListener('click', (e) => {
          if (!container.contains(e.target)) {
            closeCard();
          }
        });
      });

      // Visualizer Tab Switching
      const tabBtns = document.querySelectorAll('.vis-tab-btn');
      const panes = document.querySelectorAll('.vis-pane');
      tabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
          const targetView = btn.dataset.view;
          tabBtns.forEach(b => {
            b.classList.remove('active', 'bg-amber-500', 'text-black', 'shadow-md');
            b.classList.add('text-zinc-300');
          });
          btn.classList.add('active', 'bg-amber-500', 'text-black', 'shadow-md');
          btn.classList.remove('text-zinc-300');

          panes.forEach(pane => {
            pane.classList.remove('active');
            pane.classList.add('hidden', 'opacity-0');
          });

          const activePane = document.getElementById('pane-' + targetView);
          if (activePane) {
            activePane.classList.remove('hidden');
            setTimeout(() => {
              activePane.classList.add('active');
              activePane.classList.remove('opacity-0');
            }, 10);
          }
        });
      });
    }

    // Helper to open the full equipment modal from any hotspot button
    function openEquipmentById(id) {
      const item = equipData[id];
      if (!item) return;

      const equipModal = document.getElementById('equipModal');
      const equipModalCard = document.getElementById('modalCard');
      const equipModalTitle = document.getElementById('modalTitle');
      const equipModalCategory = document.getElementById('modalCategory');
      const equipModalImg = document.getElementById('modalImg');
      const equipModalDesc = document.getElementById('modalDesc');
      const equipModalTarget = document.getElementById('modalTarget');
      const equipModalCapacity = document.getElementById('modalCapacity');
      const equipModalBestFor = document.getElementById('modalBestFor');
      const equipModalWhatsAppBtn = document.getElementById('modalWhatsAppBtn');

      if (equipModalTitle) equipModalTitle.textContent = item.title;
      if (equipModalCategory) equipModalCategory.textContent = item.category;
      if (equipModalImg) equipModalImg.src = item.img;
      if (equipModalDesc) equipModalDesc.textContent = item.desc;
      if (equipModalTarget) equipModalTarget.textContent = item.target;
      if (equipModalCapacity) equipModalCapacity.textContent = item.capacity;
      if (equipModalBestFor) equipModalBestFor.textContent = item.bestFor;

      if (equipModalWhatsAppBtn) {
        const msg = encodeURIComponent(`Hello Sir, I saw the ${item.title} on Dragon Slayer Gym 2 and want to know more.`);
        equipModalWhatsAppBtn.href = `https://wa.me/917709339959?text=${msg}`;
      }

      if (equipModal && equipModalCard) {
        equipModal.classList.remove('hidden');
        equipModal.classList.add('flex');
        setTimeout(() => equipModalCard.classList.add('open'), 10);
      }
    }
'''

if 'initHotspots()' not in html:
    html = html.replace('// Equipment Carousel Controls', hotspot_js + '\n    initHotspots();\n\n    // Equipment Carousel Controls')

# Save updated gym-standard-website.html
with open('gym-standard-website.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Mirror to index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("gym-standard-website.html and index.html successfully updated with Interactive Mobile Hotspots!")
