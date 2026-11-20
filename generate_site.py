#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ErgoDeskCalc - Interactive Standing Desk Height, Chair Seat, Monitor Eye-Level & VESA Arm Load Calculator
+ Automated Daily Amazon Product Review Publisher
Affiliate StoreID: everythi00099-20
"""

import os
import json
import hashlib
import datetime
import urllib.request
import urllib.parse
import urllib.error

AFFILIATE_TAG = "everythi00099-20"
STATE_FILE = "posts_state.json"
OUTPUT_DIR = "public"
REVIEWS_DIR = os.path.join(OUTPUT_DIR, "reviews")
DAILY_NEW_ARTICLES = 3

# Deteksi otomatis URL GitHub Pages berdasarkan environment GitHub Actions
REPO_FULL = os.environ.get("GITHUB_REPOSITORY", "username/ergodeskcalc")
REPO_OWNER = os.environ.get("GITHUB_REPOSITORY_OWNER", REPO_FULL.split("/")[0])
REPO_NAME = REPO_FULL.split("/")[-1] if "/" in REPO_FULL else "ergodeskcalc"

if REPO_NAME.lower() == f"{REPO_OWNER.lower()}.github.io":
    BASE_URL = f"https://{REPO_OWNER.lower()}.github.io"
else:
    BASE_URL = f"https://{REPO_OWNER.lower()}.github.io/{REPO_NAME}"

INDEXNOW_KEY = hashlib.md5(f"ergodeskcalc-{AFFILIATE_TAG}".encode("utf-8")).hexdigest()


def amazon_search_url(query: str) -> str:
    encoded = urllib.parse.quote_plus(query)
    return f"https://www.amazon.com/s?k={encoded}&tag={AFFILIATE_TAG}"


# ==============================================================================
# MASTER BEST SELLER & COMPARISON CATALOG (10 FLAGSHIP ERGONOMIC OFFICE PRODUCTS)
# ==============================================================================
CORE_PRODUCTS = [
    {
        "id": "flexispot-e7-pro-standing-desk",
        "name": "FlexiSpot E7 Dual-Motor Heavy-Duty Electric Standing Desk Frame",
        "brand": "FlexiSpot",
        "category": "Standing Desk",
        "min_h_in": 22.8,
        "max_h_in": 48.4,
        "load_lbs": 355,
        "key_spec": "3-Stage Dual Motor (22.8\"–48.4\" Range)",
        "ergo_benefit": "BIFMA Certified Ultra-Low 22.8\" Minimum Height",
        "rating": "4.8",
        "reviews_count": 7840,
        "badge": "#1 Best Overall Standing Desk",
        "search_query": "FlexiSpot E7 Dual Motor Standing Desk Frame",
        "highlight": "3-stage inverted carbon steel columns fit users from 4'11\" to 6'6\" with zero wobble at standing height and 355 lb lift capacity."
    },
    {
        "id": "ergotron-lx-desk-monitor-arm",
        "name": "Ergotron LX Single Monitor Arm (Up to 34-Inch / 25 lbs VESA)",
        "brand": "Ergotron",
        "category": "Monitor Arm",
        "min_h_in": 13.0,
        "max_h_in": 24.0,
        "load_lbs": 25,
        "key_spec": "Constant Force Lift (7–25 lbs, 13\" Lift)",
        "ergo_benefit": "10,000-Cycle Tested Zero-Sag Precision Pivot",
        "rating": "4.7",
        "reviews_count": 6490,
        "badge": "#1 Pro Monitor Arm",
        "search_query": "Ergotron LX Desk Monitor Arm VESA Mount",
        "highlight": "Patented Constant Force mechanical spring technology glides effortlessly to eye level without gas-cylinder leaks over 10+ years."
    },
    {
        "id": "ergotron-hx-ultrawide-arm",
        "name": "Ergotron HX Heavy-Duty Monitor Arm for 49-Inch Ultrawide Displays",
        "brand": "Ergotron",
        "category": "Monitor Arm",
        "min_h_in": 11.5,
        "max_h_in": 23.5,
        "load_lbs": 42,
        "key_spec": "Heavy-Duty Tilt Pivot (20–42 lbs Capacity)",
        "ergo_benefit": "Supports 49\" Samsung Odyssey G9 Curved Monitors",
        "rating": "4.8",
        "reviews_count": 3120,
        "badge": "Best Ultrawide Monitor Arm",
        "search_query": "Ergotron HX Heavy Duty Ultrawide Monitor Arm",
        "highlight": "Engineered specifically for deep-curved 49-inch and 57-inch ultrawide monitors with reinforced tilt pivot and desk clamp."
    },
    {
        "id": "steelcase-leap-v2-ergonomic-chair",
        "name": "Steelcase Leap V2 Ergonomic High-Back Office Task Chair",
        "brand": "Steelcase",
        "category": "Ergonomic Chair",
        "min_h_in": 15.5,
        "max_h_in": 20.5,
        "load_lbs": 400,
        "key_spec": "LiveBack Flexing Spine + 4D Adjustable Arms",
        "ergo_benefit": "15.5\"–20.5\" Seat Pan Height + Seat Depth Slider",
        "rating": "4.6",
        "reviews_count": 4210,
        "badge": "Best All-Day Task Chair",
        "search_query": "Steelcase Leap Ergonomic Office Chair",
        "highlight": "Dynamic LiveBack backrest flexes with your lumbar curve while 4D armrests and sliding seat pan dial in exact thigh support."
    },
    {
        "id": "sihoo-doro-c300-mesh-chair",
        "name": "SIHOO Doro C300 Self-Adaptive Lumbar Mesh Ergonomic Chair",
        "brand": "SIHOO",
        "category": "Ergonomic Chair",
        "min_h_in": 17.5,
        "max_h_in": 21.5,
        "load_lbs": 300,
        "key_spec": "Dynamic Domino Lumbar + 3D Coordinated Armrests",
        "ergo_benefit": "Breathable Full-Mesh Frame & Waterfall Seat Edge",
        "rating": "4.6",
        "reviews_count": 5380,
        "badge": "Best Value Ergonomic Chair",
        "search_query": "SIHOO Doro C300 Ergonomic Office Chair Mesh",
        "highlight": "Self-tracking dynamic lumbar cushion moves automatically as you lean forward or recline to 130 degrees during long work sessions."
    },
    {
        "id": "fezibo-dual-motor-standing-desk-60",
        "name": "FEZIBO 60x24 Inch Dual-Motor Standing Desk with Keyboard Tray",
        "brand": "FEZIBO",
        "category": "Standing Desk",
        "min_h_in": 27.6,
        "max_h_in": 47.3,
        "load_lbs": 220,
        "key_spec": "Dual Motor + Slide-Out Ergonomic Keyboard Tray",
        "ergo_benefit": "4 Memory Presets + Anti-Collision Safety Sensor",
        "rating": "4.6",
        "reviews_count": 14600,
        "badge": "Best Budget Standing Desk",
        "search_query": "FEZIBO Dual Motor Standing Desk 60 Inch",
        "highlight": "Complete desktop + dual-motor frame with integrated under-desk cable management tray and lockable rolling casters."
    },
    {
        "id": "huanuo-dual-monitor-gas-spring-arm",
        "name": "HUANUO HNDS8 Dual Monitor Gas-Spring Desk Mount (Up to 32-Inch)",
        "brand": "HUANUO",
        "category": "Monitor Arm",
        "min_h_in": 10.0,
        "max_h_in": 21.0,
        "load_lbs": 19.8,
        "key_spec": "Dual Gas-Spring Arms (4.4–19.8 lbs per Arm)",
        "ergo_benefit": "360° Portrait/Landscape Rotation + USB Hub Base",
        "rating": "4.7",
        "reviews_count": 19850,
        "badge": "#1 Best Selling Dual Arm",
        "search_query": "HUANUO Dual Monitor Stand Gas Spring Arm",
        "highlight": "Dual independent gas springs clear desk clutter and align side-by-side 27-inch or 32-inch screens at identical eye level."
    },
    {
        "id": "urevo-under-desk-walking-pad",
        "name": "UREVO 2.5 HP Slim Under-Desk Walking Pad Treadmill for Standing Desks",
        "brand": "UREVO",
        "category": "Standing Accessories",
        "min_h_in": 4.8,
        "max_h_in": 4.8,
        "load_lbs": 265,
        "key_spec": "2.5 HP Quiet Motor (0.6–4.0 MPH, 4.8\" Deck)",
        "ergo_benefit": "8-Point Silicone Shock Absorption for Joint Comfort",
        "rating": "4.6",
        "reviews_count": 11200,
        "badge": "#1 Under-Desk Walking Pad",
        "search_query": "UREVO Under Desk Walking Pad Treadmill 2.5 HP",
        "highlight": "Ultra-slim 4.8-inch deck slides under any standing desk or sofa and adds effortless 10,000-step low-impact cardio while working."
    },
    {
        "id": "ergodriven-topo-anti-fatigue-mat",
        "name": "Ergodriven Topo Calculated-Terrain Anti-Fatigue Standing Desk Mat",
        "brand": "Ergodriven",
        "category": "Standing Accessories",
        "min_h_in": 1.0,
        "max_h_in": 2.8,
        "load_lbs": 350,
        "key_spec": "3D Contoured Polyurethane Terrain Surface",
        "ergo_benefit": "Prompts Micro-Movements & Calf Stretching",
        "rating": "4.8",
        "reviews_count": 9640,
        "badge": "Best Standing Desk Mat",
        "search_query": "Ergodriven Topo Anti Fatigue Standing Desk Mat",
        "highlight": "Sculpted raised perimeter ridges and central teardrop mound eliminate foot soreness and encourage unconscious posture shifts."
    },
    {
        "id": "logitech-mx-ergo-vertical-combo",
        "name": "Logitech Ergo K860 Split Keyboard & Lift Vertical Ergonomic Mouse",
        "brand": "Logitech",
        "category": "Ergonomic Peripherals",
        "min_h_in": 0.5,
        "max_h_in": 2.0,
        "load_lbs": 5,
        "key_spec": "Curved Split Keyframe + 57° Handshake Mouse Angle",
        "ergo_benefit": "Reduces Forearm Pronation & Wrist Strain by 25%",
        "rating": "4.7",
        "reviews_count": 16700,
        "badge": "Best Wrist-Relief Combo",
        "search_query": "Logitech Ergo K860 Split Keyboard Lift Vertical Mouse",
        "highlight": "Pillowed 3-layer memory foam palm rest with negative tilt legs pairs with a 57-degree vertical mouse to eliminate ulnar deviation."
    }
]


# ==============================================================================
# COMBINATORIAL ENGINE FOR 1,800 UNIQUE DAILY ERGONOMIC PRODUCT REVIEW ARTICLES
# ==============================================================================
BRANDS_MATRIX = [
    ("FlexiSpot", "3-Stage Dual-Motor Telescoping Steel Frame & 355 lb Lift Rating"),
    ("UPLIFT Desk", "Commercial-Grade C-Frame Crossbar Stability & 15-Year Warranty"),
    ("Ergotron", "Patented Constant Force Mechanical Spring & 10,000-Cycle Precision Pivot"),
    ("Steelcase", "LiveBack Dynamic Spinal Flexure & 4-Way Micro-Adjustable Armrests"),
    ("SIHOO", "Self-Adaptive Domino Lumbar Architecture & Breathable Dragon Mesh"),
    ("HUANUO", "Heavy-Duty Reinforced Gas-Spring Cylinder & Dual C-Clamp Base"),
    ("VIVO", "Solid Steel Articulating VESA Counterbalance & Integrated Cable Clips"),
    ("FEZIBO", "Dual-Motor Quiet 45dB Drive & Anti-Collision Gyro Sensor"),
    ("Marsail", "One-Piece Solid Laminate Desktop & 4-Memory Digital Handset"),
    ("UREVO", "2.5 HP Whisper-Quiet Brushless Motor & 5-Layer Shock-Absorbing Belt"),
    ("Ergodriven", "Calculated 3D Terrain Polyurethane Foam & Single-Foot Slide Heel"),
    ("Branch", "Commercial BIFMA Ergonomic Calibration & Anodized Aluminum Base"),
    ("Logitech Ergo", "57-Degree Neutral Handshake Geometry & Split Curved Keyframe"),
    ("Autonomous", "High-Torque Dual-Motor Lift Columns & 7-Year Steel Frame Rating"),
    ("Humanscale", "Weight-Sensitive Counterbalance Recline & Knob-Free Automatic Fit"),
]

MODELS_MATRIX = [
    ("Dual-Motor 3-Stage Electric Standing Desk (22.8\"–48.4\")", 22.8, 48.4, 355, "Standing Desk", "Dual-Motor 3-Stage Columns"),
    ("L-Shaped Corner Triple-Motor Standing Desk (24\"–49\")", 24.0, 49.0, 440, "Standing Desk", "Triple-Motor 3-Leg Stability"),
    ("Compact 48x24 Home Office Electric Standing Desk", 27.5, 47.2, 220, "Standing Desk", "Small-Space Dual Motor"),
    ("Heavy-Duty 49-Inch Ultrawide VESA Monitor Arm (42 lbs)", 11.5, 23.5, 42, "Monitor Arm", "Ultrawide Counterbalance Tilt"),
    ("Single Gas-Spring Monitor Mount (Up to 34\" / 26 lbs)", 10.0, 22.0, 26, "Monitor Arm", "Full-Motion 360° Gas Spring"),
    ("Dual Side-by-Side Articulating Monitor Arm (2x 32\")", 10.0, 21.5, 40, "Monitor Arm", "Independent Dual VESA Arms"),
    ("High-Back Mesh Ergonomic Chair with Dynamic Lumbar", 17.0, 21.5, 330, "Ergonomic Chair", "Seat-Depth Slider + 4D Arms"),
    ("Big & Tall 400 lb Heavy-Duty Ergonomic Task Chair", 17.5, 22.0, 400, "Ergonomic Chair", "Wide 22\" Cushion + Steel Base"),
    ("Petite-Friendly Low-Seat Ergonomic Office Chair", 15.5, 19.5, 300, "Ergonomic Chair", "15.5\" Low-Drop Gas Cylinder"),
    ("2.5 HP Slim Under-Desk Walking Pad Treadmill", 4.8, 4.8, 265, "Standing Accessories", "4.8\" Ultra-Low Deck Profile"),
    ("3D Contoured Anti-Fatigue Standing Desk Floor Mat", 1.0, 2.8, 350, "Standing Accessories", "High-Density Beveled Terrain"),
    ("Split Ergonomic Keyboard & 57° Vertical Mouse Kit", 0.5, 2.0, 5, "Ergonomic Peripherals", "Negative-Tilt Palm Rest"),
]

USER_PROFILES_MATRIX = [
    ("Tall Users (6'1\" to 6'6\") Needing Extra Standing Elevation", 75, "prevents hunched shoulders by reaching full 46+ inch standing elbow height cleanly"),
    ("Petite & Shorter Users (4'11\" to 5'4\") Needing Low Seated Desk Drop", 62, "eliminates shoulder shrugging by dropping low enough for 90-degree relaxed forearms"),
    ("Average-Height Remote Workers (5'7\" to 5'11\") Working 8+ Hours Daily", 69, "maintains neutral spine alignment across seamless sit-to-stand transitions all day"),
    ("Software Engineers & Programmers Running Dual 32-Inch 4K Monitors", 70, "holds heavy multi-monitor arrays rock-steady at exact eye level without screen bounce"),
    ("Ultrawide 49-Inch Curved Gaming & Day-Trading Battlestations", 71, "absorbs forward center-of-gravity torque so curved screens never droop"),
    ("Small Apartment & Bedroom Corner Home Office Setups", 66, "reclaims valuable desk surface area while maintaining proper 24-inch viewing distance"),
    ("Lower Back Pain & Sciatica Relief Active Sit-Stand Workflows", 68, "offloads lumbar disc compression by alternating seated support with active standing"),
    ("Walking-Pad Active Desk Workers Logging 10,000 Steps Per Shift", 70, "adds 5 inches of extra standing height clearance to match treadmill deck thickness"),
    ("Video Editors, Architects & Creative Studio Colorists", 69, "stabilizes heavy audio interfaces, studio monitors, and dual color-calibrated displays"),
    ("Shared Family & Dual-User Hot-Desking Workstations", 67, "stores 4 instant height presets so two different users switch posture in 8 seconds"),
]


def get_article_blueprint(index: int) -> dict:
    """Secara deterministik menghasilkan artikel review produk ergonomi kantor unik berdasarkan indeks."""
    b_idx = index % len(BRANDS_MATRIX)
    m_idx = (index // len(BRANDS_MATRIX)) % len(MODELS_MATRIX)
    u_idx = (index // (len(BRANDS_MATRIX) * len(MODELS_MATRIX))) % len(USER_PROFILES_MATRIX)

    brand_name, brand_tech = BRANDS_MATRIX[b_idx]
    model_name, min_h, max_h, load_lbs, category, core_mech = MODELS_MATRIX[m_idx]
    profile_title, height_in, profile_benefit = USER_PROFILES_MATRIX[u_idx]

    ft = height_in // 12
    inch = height_in % 12
    cm = round(height_in * 2.54)
    sit_desk = round(height_in * 0.405 + 0.8, 1)
    stand_desk = round(height_in * 0.625 + 0.8, 1)
    chair_h = round(height_in * 0.25 + 0.8, 1)

    slug = f"review-{brand_name.lower().replace(' ', '-')}-{model_name.lower().replace('\"', 'in').replace('(', '').replace(')', '').replace('/', '').replace(' ', '-')}-{index + 1}"
    slug = "".join(c if c.isalnum() or c == "-" else "" for c in slug)
    while "--" in slug:
        slug = slug.replace("--", "-")

    title = f"{brand_name} {model_name} Review: Ergonomic Fit for {profile_title}"
    search_q = f"{brand_name} {model_name}"

    return {
        "index": index,
        "slug": slug,
        "title": title,
        "brand": brand_name,
        "brand_tech": brand_tech,
        "model_name": model_name,
        "category": category,
        "min_h": min_h,
        "max_h": max_h,
        "load_lbs": load_lbs,
        "core_mech": core_mech,
        "profile_title": profile_title,
        "height_label": f"{ft}'{inch}\" ({cm} cm)",
        "height_in": height_in,
        "sit_desk": sit_desk,
        "stand_desk": stand_desk,
        "chair_h": chair_h,
        "profile_benefit": profile_benefit,
        "rating": "4.8" if (index % 2 == 0) else "4.7",
        "search_query": search_q,
        "affiliate_url": amazon_search_url(search_q),
    }


def load_and_advance_state() -> tuple[list[dict], list[dict]]:
    """Memuat daftar artikel dari posts_state.json dan menambahkan 3 artikel review unik setiap hari."""
    today_str = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")

    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            state = json.load(f)
    else:
        state = {
            "last_run_date": "",
            "next_index": 0,
            "published_articles": []
        }

    newly_added = []
    if len(state["published_articles"]) == 0:
        count_to_add = 6  # Inisialisasi perdana 6 artikel
    else:
        count_to_add = DAILY_NEW_ARTICLES  # Tambah 3 artikel berbeda setiap hari

    for _ in range(count_to_add):
        idx = state["next_index"]
        bp = get_article_blueprint(idx)
        entry = {
            "index": idx,
            "slug": bp["slug"],
            "date": today_str,
            "title": bp["title"]
        }
        state["published_articles"].append(entry)
        newly_added.append({**bp, "date": today_str})
        state["next_index"] = idx + 1

    state["last_run_date"] = today_str

    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)

    all_articles = []
    for item in reversed(state["published_articles"]):
        bp = get_article_blueprint(item["index"])
        bp["date"] = item["date"]
        all_articles.append(bp)

    return all_articles, newly_added


# ==============================================================================
# SHARED CSS — INDUSTRIAL GREY BACKGROUND THEME
# ==============================================================================
GLOBAL_CSS = """
:root {
  --bg-page: #cbd5e1;        /* Abu-abu utama (Grey background sesuai instruksi) */
  --bg-section: #e2e8f0;     /* Abu-abu medium untuk kontainer seksi */
  --bg-card: #f1f5f9;        /* Abu-abu terang untuk kartu konten & kalkulator */
  --bg-dark: #1e293b;        /* Abu-abu slate gelap untuk header & tabel */
  --bg-darker: #0f172a;      /* Slate pekat untuk banner atas & footer */
  --border-grey: #94a3b8;    /* Garis tepi abu-abu tegas */
  --text-main: #0f172a;
  --text-muted: #334155;
  --accent-amazon: #ff9900;
  --accent-blue: #0369a1;
  --accent-green: #15803d;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  background-color: var(--bg-page);
  color: var(--text-main);
  line-height: 1.6;
}
a { color: var(--accent-blue); text-decoration: none; }
.container { max-width: 1240px; margin: 0 auto; padding: 0 18px; }

/* TOP PROMO BANNER */
.top-promo-banner {
  background: linear-gradient(90deg, #0f172a 0%, #334155 50%, #1e293b 100%);
  color: #ffffff;
  padding: 12px 16px;
  border-bottom: 3px solid var(--accent-amazon);
  text-align: center;
  font-size: 0.94rem;
}
.top-promo-banner .badge-live {
  background: var(--accent-amazon);
  color: #0f172a;
  font-weight: 900;
  padding: 3px 10px;
  border-radius: 4px;
  margin-right: 10px;
  text-transform: uppercase;
  font-size: 0.78rem;
}
.top-promo-banner a.banner-cta {
  display: inline-block;
  margin-left: 12px;
  background: #38bdf8;
  color: #0f172a;
  font-weight: 800;
  padding: 4px 14px;
  border-radius: 5px;
  text-decoration: none;
}
.top-promo-banner a.banner-cta:hover { background: #7dd3fc; }

/* STICKY HEADER */
header.site-header {
  background-color: var(--bg-dark);
  color: #f8fafc;
  padding: 16px 0;
  box-shadow: 0 3px 10px rgba(0,0,0,0.22);
  position: sticky;
  top: 0;
  z-index: 100;
}
.nav-flex {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;
  gap: 14px;
}
.brand-logo {
  font-size: 1.55rem;
  font-weight: 900;
  color: #ffffff;
  letter-spacing: -0.5px;
}
.brand-logo span { color: var(--accent-amazon); }
.nav-links {
  display: flex;
  flex-wrap: wrap;
  gap: 14px;
  list-style: none;
}
.nav-links a {
  color: #e2e8f0;
  font-weight: 600;
  font-size: 0.92rem;
  padding: 6px 10px;
  border-radius: 5px;
}
.nav-links a:hover { background: #334155; color: var(--accent-amazon); }

/* HERO BANNER */
.hero-banner {
  background: linear-gradient(135deg, #334155 0%, #1e293b 100%);
  color: #f8fafc;
  padding: 34px 26px;
  margin: 24px 0;
  border-radius: 12px;
  border: 2px solid #64748b;
  box-shadow: 0 8px 20px rgba(0,0,0,0.14);
}
.hero-grid {
  display: grid;
  grid-template-columns: 1.25fr 0.75fr;
  gap: 24px;
  align-items: center;
}
@media (max-width: 860px) { .hero-grid { grid-template-columns: 1fr; } }
.hero-banner h1 { font-size: 2.05rem; line-height: 1.22; margin-bottom: 12px; color: #ffffff; }
.hero-banner p { color: #cbd5e1; font-size: 1.02rem; margin-bottom: 18px; }
.hero-deal-box {
  background: #0f172a;
  border: 2px solid var(--accent-amazon);
  padding: 20px;
  border-radius: 10px;
  text-align: center;
}
.hero-deal-box h3 { color: var(--accent-amazon); margin-bottom: 8px; font-size: 1.18rem; }

/* BUTTONS */
.btn-amazon {
  display: inline-block;
  background: linear-gradient(180deg, #ffd814 0%, #ff9900 100%);
  color: #0f172a !important;
  font-weight: 800;
  padding: 11px 18px;
  border-radius: 6px;
  border: 1px solid #d97706;
  text-align: center;
  cursor: pointer;
  text-decoration: none;
  box-shadow: 0 2px 5px rgba(0,0,0,0.15);
}
.btn-amazon:hover { background: linear-gradient(180deg, #f7ca00 0%, #e68a00 100%); }
.btn-outline {
  display: inline-block;
  padding: 9px 14px;
  border: 2px solid #1e293b;
  color: #0f172a;
  font-weight: 700;
  border-radius: 6px;
  font-size: 0.88rem;
}
.btn-outline:hover { background: #1e293b; color: #ffffff; }

/* GREY SECTION WRAPPERS */
.grey-section {
  background-color: var(--bg-section);
  border: 1px solid var(--border-grey);
  border-radius: 12px;
  padding: 26px;
  margin-bottom: 26px;
  box-shadow: 0 3px 8px rgba(0,0,0,0.06);
}
.section-title {
  font-size: 1.55rem;
  font-weight: 800;
  color: #0f172a;
  margin-bottom: 8px;
  border-left: 6px solid var(--accent-amazon);
  padding-left: 12px;
}
.section-sub { color: var(--text-muted); margin-bottom: 20px; font-size: 0.96rem; }

/* INTERACTIVE ERGONOMICS CALCULATOR */
.calc-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 24px;
}
@media (max-width: 860px) { .calc-grid { grid-template-columns: 1fr; } }
.calc-panel {
  background: var(--bg-card);
  border: 1px solid var(--border-grey);
  padding: 22px;
  border-radius: 10px;
}
.preset-row { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 16px; }
.preset-btn {
  background: #cbd5e1;
  border: 1px solid #64748b;
  color: #0f172a;
  padding: 7px 12px;
  border-radius: 6px;
  font-size: 0.83rem;
  font-weight: 700;
  cursor: pointer;
}
.preset-btn:hover { background: #94a3b8; }
.form-row { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
.form-group { margin-bottom: 14px; }
.form-group label { display: block; font-weight: 700; margin-bottom: 5px; font-size: 0.9rem; color: #1e293b; }
.form-group input, .form-group select {
  width: 100%;
  padding: 10px 12px;
  border: 1px solid #64748b;
  border-radius: 6px;
  background: #ffffff;
  font-size: 0.98rem;
  color: #0f172a;
}
.metrics-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 16px; }
.metric-card {
  background: #e2e8f0;
  border: 1px solid #94a3b8;
  padding: 14px;
  border-radius: 8px;
  text-align: center;
}
.metric-card .val { font-size: 1.48rem; font-weight: 900; color: #0f172a; }
.metric-card .lbl { font-size: 0.77rem; font-weight: 700; color: #334155; text-transform: uppercase; }
.rec-box {
  background: #ffffff;
  border: 2px solid var(--accent-green);
  border-radius: 8px;
  padding: 16px;
  margin-top: 12px;
}
.rec-box h4 { color: var(--accent-green); font-size: 1.04rem; margin-bottom: 6px; }

/* SEARCH & FILTER BAR */
.search-bar { display: flex; flex-wrap: wrap; gap: 12px; margin-bottom: 18px; }
.search-input {
  flex: 1;
  min-width: 240px;
  padding: 12px 15px;
  border: 2px solid #475569;
  border-radius: 8px;
  font-size: 1rem;
  background: #ffffff;
}
.filter-select {
  padding: 12px 15px;
  border: 2px solid #475569;
  border-radius: 8px;
  font-size: 0.95rem;
  background: #ffffff;
  font-weight: 700;
}

/* PRODUCT & DAILY ARTICLE CARDS */
.product-grid, .articles-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 18px;
}
.product-card, .article-card {
  background: var(--bg-card);
  border: 1px solid var(--border-grey);
  border-radius: 10px;
  padding: 20px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.badge-tag {
  display: inline-block;
  background: #1e293b;
  color: var(--accent-amazon);
  font-size: 0.75rem;
  font-weight: 800;
  padding: 4px 10px;
  border-radius: 4px;
  margin-bottom: 10px;
  align-self: flex-start;
  text-transform: uppercase;
}
.spec-box {
  list-style: none;
  margin: 10px 0 14px;
  font-size: 0.88rem;
  background: #e2e8f0;
  padding: 10px 12px;
  border-radius: 6px;
}
.spec-box li { margin-bottom: 4px; }

/* COMPARISON TABLE */
.table-wrap { overflow-x: auto; }
table.comp-table {
  width: 100%;
  border-collapse: collapse;
  background: #f8fafc;
  border-radius: 8px;
  overflow: hidden;
}
table.comp-table th {
  background: #1e293b;
  color: #ffffff;
  text-align: left;
  padding: 13px 12px;
  font-size: 0.86rem;
  text-transform: uppercase;
}
table.comp-table td {
  padding: 12px;
  border-bottom: 1px solid #cbd5e1;
  font-size: 0.91rem;
}
table.comp-table tr:nth-child(even) { background: #e2e8f0; }

/* FAQ ACCORDION */
details.faq-item {
  background: var(--bg-card);
  border: 1px solid var(--border-grey);
  border-radius: 8px;
  padding: 14px 18px;
  margin-bottom: 12px;
}
details.faq-item summary { font-weight: 800; font-size: 1.02rem; cursor: pointer; color: #0f172a; }
details.faq-item p { margin-top: 10px; color: #334155; font-size: 0.95rem; }

/* SITEMAP DIRECTORY */
.sitemap-columns { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; }
.sitemap-box { background: var(--bg-card); border: 1px solid var(--border-grey); padding: 18px; border-radius: 8px; }
.sitemap-box h3 { margin-bottom: 10px; font-size: 1.1rem; color: #0f172a; }
.sitemap-box ul { padding-left: 18px; font-size: 0.9rem; line-height: 1.8; }

/* FOOTER */
footer.site-footer {
  background: var(--bg-darker);
  color: #cbd5e1;
  padding: 36px 0;
  margin-top: 40px;
  border-top: 4px solid var(--accent-amazon);
  font-size: 0.9rem;
}
.footer-links { display: flex; flex-wrap: wrap; gap: 16px; margin-bottom: 14px; }
.footer-links a { color: #f8fafc; font-weight: 600; }
"""


# ==============================================================================
# HTML PAGE GENERATORS
# ==============================================================================
def build_article_page(article: dict, recent_articles: list[dict]) -> str:
    """Membangun halaman HTML artikel review produk ergonomi harian lengkap dengan kalkulator & Schema SEO."""
    related_links = ""
    for rel in recent_articles[:8]:
        if rel["slug"] == article["slug"]:
            continue
        related_links += f"""
        <li>
          <a href="{BASE_URL}/reviews/{rel['slug']}.html"><strong>{rel['title']}</strong></a>
          <span> ({rel['category']} | Load: {rel['load_lbs']} lbs — {rel['date']})</span>
        </li>
        """

    heights_chart = [
        ("5'2\" (157 cm)", 62),
        ("5'6\" (168 cm)", 66),
        ("5'10\" (178 cm)", 70),
        ("6'1\" (185 cm)", 73),
        ("6'4\" (193 cm)", 76),
    ]
    chart_rows = ""
    for label, h_in in heights_chart:
        s_desk = round(h_in * 0.405 + 0.8, 1)
        st_desk = round(h_in * 0.625 + 0.8, 1)
        ch_h = round(h_in * 0.25 + 0.8, 1)
        chart_rows += f"""
        <tr>
          <td><strong>{label}</strong></td>
          <td>{ch_h}\" ({round(ch_h * 2.54)} cm)</td>
          <td>{s_desk}\" ({round(s_desk * 2.54)} cm)</td>
          <td>{st_desk}\" ({round(st_desk * 2.54)} cm)</td>
        </tr>
        """

    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": f"Is the {article['brand']} {article['model_name']} suitable for {article['profile_title']}?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": f"Yes. With a rated load capacity of {article['load_lbs']} lbs and {article['core_mech']}, the {article['brand']} {article['model_name']} {article['profile_benefit']}."
                }
            },
            {
                "@type": "Question",
                "name": f"What desk height does a {article['height_label']} user need?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": f"According to ANSI/BIFMA anthropometric standards, a {article['height_label']} user needs an optimal seated desk height of approximately {article['sit_desk']} inches and a standing desk height of {article['stand_desk']} inches."
                }
            }
        ]
    }

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{article['title']} ({article['date']} Ergonomic Fit &amp; Load Test)</title>
  <meta name="description" content="Hands-on ergonomic fit review of the {article['brand']} {article['model_name']} ({article['load_lbs']} lbs capacity) for {article['profile_title']}. Includes desk height chart &amp; Amazon deals." />
  <link rel="canonical" href="{BASE_URL}/reviews/{article['slug']}.html" />
  <meta property="og:title" content="{article['title']}" />
  <meta property="og:description" content="Rated at {article['load_lbs']} lbs with {article['brand_tech']}. Ergonomic calibration for {article['height_label']}." />
  <meta property="og:type" content="article" />
  <meta property="og:url" content="{BASE_URL}/reviews/{article['slug']}.html" />
  <style>{GLOBAL_CSS}</style>
  <script type="application/ld+json">{json.dumps(faq_schema)}</script>
</head>
<body>
  <div class="top-promo-banner">
    <span class="badge-live">HOME OFFICE DEAL</span>
    Check Live Amazon Price &amp; Instant Coupon on <strong>{article['brand']} {article['model_name']}</strong>
    <a class="banner-cta" href="{article['affiliate_url']}" target="_blank" rel="nofollow sponsored noopener">Check Price on Amazon &rarr;</a>
  </div>

  <header class="site-header">
    <div class="container nav-flex">
      <a href="{BASE_URL}/index.html" class="brand-logo">ErgoDesk<span>Calc</span></a>
      <ul class="nav-links">
        <li><a href="{BASE_URL}/index.html#calculator">Ergonomic Calculator</a></li>
        <li><a href="{BASE_URL}/index.html#search-section">Search Products</a></li>
        <li><a href="{BASE_URL}/index.html#bestsellers">Best Sellers</a></li>
        <li><a href="{BASE_URL}/index.html#comparison">Comparison Table</a></li>
        <li><a href="{BASE_URL}/index.html#daily-reviews">Daily Reviews</a></li>
        <li><a href="{BASE_URL}/sitemap.html">Site Map</a></li>
      </ul>
    </div>
  </header>

  <main class="container" style="margin-top:24px;">
    <article class="grey-section">
      <div style="font-size:0.82rem; font-weight:700; color:#334155; text-transform:uppercase; margin-bottom:6px;">
        Published: {article['date']} &bull; Category: {article['category']} &bull; Verified Rating: ★ {article['rating']}/5.0
      </div>
      <h1 style="font-size:1.95rem; margin-bottom:14px; color:#0f172a;">{article['title']}</h1>
      <p style="font-size:1.05rem; color:#334155; margin-bottom:20px;">
        Configuring a pain-free workstation for <strong>{article['profile_title']}</strong> requires matching exact anthropometric dimensions—specifically a seated desk height near <strong>{article['sit_desk']} inches</strong>, chair seat height near <strong>{article['chair_h']} inches</strong>, and standing desk elevation around <strong>{article['stand_desk']} inches</strong>. In this review, we examine how the <strong>{article['brand']} {article['model_name']}</strong> ({article['load_lbs']} lbs rated load) {article['profile_benefit']}.
      </p>

      <div class="hero-deal-box" style="margin-bottom:24px; text-align:left; display:flex; flex-wrap:wrap; justify-content:space-between; align-items:center; gap:16px;">
        <div>
          <h3 style="margin-bottom:4px;">{article['brand']} {article['model_name']} — Amazon Availability</h3>
          <p style="color:#cbd5e1; font-size:0.93rem;">{article['brand_tech']} | Height Range: {article['min_h']}\"–{article['max_h']}\" | Rated Load: {article['load_lbs']} lbs</p>
        </div>
        <a class="btn-amazon" href="{article['affiliate_url']}" target="_blank" rel="nofollow sponsored noopener">Check Current Price on Amazon &rarr;</a>
      </div>

      <h2 class="section-title">1. Mechanical Specs &amp; Ergonomic Calibration</h2>
      <div class="table-wrap" style="margin:16px 0 26px;">
        <table class="comp-table">
          <thead>
            <tr>
              <th>Specification</th>
              <th>Rated Measurement</th>
              <th>Posture &amp; Stability Impact</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Height / Vertical Range</strong></td>
              <td>{article['min_h']}\" to {article['max_h']}\"</td>
              <td>Matches target ergonomic zone for {article['height_label']} users</td>
            </tr>
            <tr>
              <td><strong>Maximum Load Capacity</strong></td>
              <td>{article['load_lbs']} lbs</td>
              <td>Zero sag or front-to-back wobble under full workstation hardware</td>
            </tr>
            <tr>
              <td><strong>Core Engineering Mechanism</strong></td>
              <td>{article['core_mech']}</td>
              <td>{article['brand_tech']}</td>
            </tr>
            <tr>
              <td><strong>Target Posture Profile</strong></td>
              <td>{article['profile_title']}</td>
              <td>Designed for neutral 90-degree elbows and relaxed trapezius muscles</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2 class="section-title">2. Quick Personal Height Checker for {article['brand']}</h2>
      <p class="section-sub">Enter your height in inches below (e.g., 70 inches = 5'10\") to verify your ideal sitting and standing heights:</p>
      <div class="calc-panel" style="margin-bottom:26px;">
        <div class="calc-grid">
          <div class="form-group">
            <label for="artHeightIn">Your Height (Total Inches):</label>
            <input type="number" id="artHeightIn" value="{article['height_in']}" min="56" max="82" step="1" oninput="calcArticleErgo()" />
            <p style="font-size:0.86rem; color:#334155; margin-top:6px;">Tip: 5'4\" = 64 in &bull; 5'8\" = 68 in &bull; 6'0\" = 72 in</p>
          </div>
          <div class="metric-card">
            <div class="lbl">Your Ideal Sit / Stand Desk Height</div>
            <div class="val" id="artErgoOut">Sit: {article['sit_desk']}\" | Stand: {article['stand_desk']}\"</div>
            <div style="margin-top:10px;">
              <a class="btn-amazon" href="{article['affiliate_url']}" target="_blank" rel="nofollow sponsored noopener">Shop {article['brand']} on Amazon</a>
            </div>
          </div>
        </div>
      </div>

      <h2 class="section-title">3. ANSI/BIFMA Desk &amp; Chair Height Reference Chart</h2>
      <div class="table-wrap" style="margin:16px 0 26px;">
        <table class="comp-table">
          <thead>
            <tr>
              <th>User Height</th>
              <th>Chair Seat Height</th>
              <th>Seated Desk Height</th>
              <th>Standing Desk Height</th>
            </tr>
          </thead>
          <tbody>
            {chart_rows}
          </tbody>
        </table>
      </div>

      <h2 class="section-title">4. Pros, Cons &amp; Ergonomic Verdict</h2>
      <div class="calc-grid" style="margin:16px 0 26px;">
        <div class="calc-panel" style="border-left:5px solid #15803d;">
          <h3 style="color:#15803d; margin-bottom:10px;">Key Strengths (Pros)</h3>
          <ul style="padding-left:18px; font-size:0.94rem;">
            <li><strong>{article['brand_tech']}</strong> delivers dependable long-term structural rigidity.</li>
            <li>Generous <strong>{article['load_lbs']} lbs load rating</strong> leaves plenty of headroom for multi-monitor setups.</li>
            <li>Well calibrated for <strong>{article['profile_title']}</strong>.</li>
          </ul>
        </div>
        <div class="calc-panel" style="border-left:5px solid #b91c1c;">
          <h3 style="color:#b91c1c; margin-bottom:10px;">Things to Consider (Cons)</h3>
          <ul style="padding-left:18px; font-size:0.94rem;">
            <li>Using an under-desk walking pad adds ~4.5 to 5 inches to your standing height—verify maximum elevation before ordering.</li>
            <li>Pair with a dedicated cable management tray to prevent tension when switching from sit to stand.</li>
          </ul>
        </div>
      </div>

      <div class="hero-deal-box">
        <h3>Ready to Build a Pain-Free Setup for {article['profile_title']}?</h3>
        <p style="color:#cbd5e1; margin-bottom:14px;">Compare live Amazon discounts, finish options, and verified buyer photos today.</p>
        <a class="btn-amazon" href="{article['affiliate_url']}" target="_blank" rel="nofollow sponsored noopener">View {article['brand']} {article['model_name']} on Amazon &rarr;</a>
      </div>
    </article>

    <section class="grey-section">
      <h2 class="section-title">More Daily Ergonomic Desk, Chair &amp; Monitor Arm Reviews</h2>
      <ul style="padding-left:20px; line-height:1.9;">
        {related_links}
      </ul>
    </section>
  </main>

  <footer class="site-footer">
    <div class="container">
      <div class="footer-links">
        <a href="{BASE_URL}/index.html">Home &amp; Ergonomic Calculator</a>
        <a href="{BASE_URL}/index.html#bestsellers">Best Sellers</a>
        <a href="{BASE_URL}/index.html#comparison">Comparison Chart</a>
        <a href="{BASE_URL}/sitemap.html">HTML Site Map</a>
        <a href="{BASE_URL}/sitemap.xml">XML Sitemap</a>
        <a href="{BASE_URL}/feed.xml">RSS Feed</a>
      </div>
      <p>Affiliate Disclosure: ErgoDeskCalc participates in the Amazon Services LLC Associates Program (StoreID: {AFFILIATE_TAG}). As an Amazon Associate, we earn from qualifying purchases.</p>
    </div>
  </footer>

  <script>
    function calcArticleErgo() {{
      var h = parseFloat(document.getElementById('artHeightIn').value) || 68;
      var sit = (h * 0.405 + 0.8).toFixed(1);
      var stand = (h * 0.625 + 0.8).toFixed(1);
      document.getElementById('artErgoOut').textContent = 'Sit: ' + sit + '\" | Stand: ' + stand + '\"';
    }}
  </script>
</body>
</html>"""


def build_html_sitemap_page(all_articles: list[dict]) -> str:
    """Membangun halaman direktori HTML Site Map lengkap (sitemap.html)."""
    article_links = ""
    for art in all_articles:
        article_links += f"""
        <li>
          <a href="{BASE_URL}/reviews/{art['slug']}.html"><strong>{art['title']}</strong></a>
          <span> — {art['category']} ({art['load_lbs']} lbs | Published {art['date']})</span>
        </li>
        """

    product_links = ""
    for p in CORE_PRODUCTS:
        product_links += f"""
        <li>
          <a href="{amazon_search_url(p['search_query'])}" target="_blank" rel="nofollow sponsored noopener">{p['name']} ({p['key_spec']})</a>
          <span> — {p['badge']}</span>
        </li>
        """

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Complete Site Map — ErgoDeskCalc Standing Desk, Chair &amp; Monitor Arm Calculator</title>
  <meta name="description" content="Complete HTML Site Map indexing all ergonomic standing desk calculators, monitor distance tools, comparison tables, and {len(all_articles)} daily product reviews." />
  <link rel="canonical" href="{BASE_URL}/sitemap.html" />
  <style>{GLOBAL_CSS}</style>
</head>
<body>
  <header class="site-header">
    <div class="container nav-flex">
      <a href="{BASE_URL}/index.html" class="brand-logo">ErgoDesk<span>Calc</span></a>
      <ul class="nav-links">
        <li><a href="{BASE_URL}/index.html#calculator">Ergonomic Calculator</a></li>
        <li><a href="{BASE_URL}/index.html#bestsellers">Best Sellers</a></li>
        <li><a href="{BASE_URL}/index.html#comparison">Comparison Table</a></li>
        <li><a href="{BASE_URL}/index.html#daily-reviews">Daily Reviews</a></li>
        <li><a href="{BASE_URL}/sitemap.xml">XML Sitemap</a></li>
      </ul>
    </div>
  </header>

  <main class="container" style="margin-top:24px;">
    <section class="grey-section">
      <h1 class="section-title">ErgoDeskCalc — Complete HTML Site Map &amp; Archive</h1>
      <p class="section-sub">Direct index of all ergonomic workstation calculators, comparison tables, XML feeds, and {len(all_articles)} automated daily product reviews.</p>

      <div class="sitemap-columns" style="margin-bottom:24px;">
        <div class="sitemap-box">
          <h3>Core Calculators &amp; Sections</h3>
          <ul>
            <li><a href="{BASE_URL}/index.html">Homepage &amp; 4-in-1 Ergonomic Desk Calculator</a></li>
            <li><a href="{BASE_URL}/index.html#calculator">Standing Desk, Chair, Monitor Distance &amp; VESA Arm Load Tool</a></li>
            <li><a href="{BASE_URL}/index.html#search-section">Real-Time Home Office Gear Search &amp; Filter</a></li>
            <li><a href="{BASE_URL}/index.html#bestsellers">Top 10 Best-Selling Ergonomic Office Products</a></li>
            <li><a href="{BASE_URL}/index.html#comparison">Side-by-Side Technical Comparison Table</a></li>
            <li><a href="{BASE_URL}/index.html#faq">OSHA &amp; ANSI/BIFMA Ergonomics FAQ</a></li>
          </ul>
        </div>
        <div class="sitemap-box">
          <h3>Search Engine &amp; Syndication Feeds</h3>
          <ul>
            <li><a href="{BASE_URL}/sitemap.xml">Primary XML Sitemap (sitemap.xml)</a></li>
            <li><a href="{BASE_URL}/feed.xml">Automated Daily Review RSS 2.0 Feed (feed.xml)</a></li>
            <li><a href="{BASE_URL}/robots.txt">Crawler Directives (robots.txt)</a></li>
          </ul>
        </div>
      </div>

      <div class="sitemap-box" style="margin-bottom:24px;">
        <h3>All Daily Ergonomic Product Review Articles ({len(all_articles)} Indexed Pages)</h3>
        <ul>
          {article_links}
        </ul>
      </div>

      <div class="sitemap-box">
        <h3>Direct Amazon Best-Seller Links (StoreID: {AFFILIATE_TAG})</h3>
        <ul>
          {product_links}
        </ul>
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <div class="container">
      <p>&copy; {datetime.datetime.now(datetime.timezone.utc).year} ErgoDeskCalc (Amazon StoreID: {AFFILIATE_TAG}). <a href="{BASE_URL}/index.html" style="color:#ffffff;">Return to Ergonomic Calculator</a></p>
    </div>
  </footer>
</body>
</html>"""


def build_index_page(all_articles: list[dict]) -> str:
    """Membangun halaman utama (index.html) dengan Kalkulator Ergonomi 4-in-1, Banner, Search, Best Sellers, Comparison, Daily Reviews, FAQ, dan Site Map."""
    bestsellers_cards = ""
    for p in CORE_PRODUCTS:
        aff_url = amazon_search_url(p["search_query"])
        bestsellers_cards += f"""
        <div class="product-card" data-search="{p['name'].lower()} {p['brand'].lower()} {p['category'].lower()} {p['highlight'].lower()}" data-category="{p['category']}">
          <div>
            <span class="badge-tag">{p['badge']}</span>
            <h3 style="font-size:1.14rem; margin-bottom:8px;">{p['name']}</h3>
            <p style="font-size:0.88rem; color:#334155; margin-bottom:8px;">{p['highlight']}</p>
            <ul class="spec-box">
              <li><strong>Height / Lift Range:</strong> {p['min_h_in']}\" – {p['max_h_in']}\"</li>
              <li><strong>Max Load Capacity:</strong> {p['load_lbs']} lbs</li>
              <li><strong>Key Hardware Spec:</strong> {p['key_spec']}</li>
              <li><strong>Ergonomic Highlight:</strong> {p['ergo_benefit']}</li>
              <li><strong>Buyer Rating:</strong> ★ {p['rating']}/5 ({p['reviews_count']}+ reviews)</li>
            </ul>
          </div>
          <a class="btn-amazon" href="{aff_url}" target="_blank" rel="nofollow sponsored noopener">Check Price on Amazon &rarr;</a>
        </div>
        """

    comparison_rows = ""
    for p in CORE_PRODUCTS:
        aff_url = amazon_search_url(p["search_query"])
        comparison_rows += f"""
        <tr>
          <td><strong>{p['name']}</strong><br/><span style="font-size:0.78rem; color:#334155;">{p['badge']}</span></td>
          <td>{p['category']}</td>
          <td><strong>{p['min_h_in']}\"–{p['max_h_in']}\"</strong></td>
          <td>{p['load_lbs']} lbs</td>
          <td>{p['key_spec']}</td>
          <td>{p['ergo_benefit']}</td>
          <td>★ {p['rating']}</td>
          <td><a class="btn-amazon" style="padding:7px 12px; font-size:0.82rem;" href="{aff_url}" target="_blank" rel="nofollow sponsored noopener">View Deal</a></td>
        </tr>
        """

    daily_cards = ""
    for art in all_articles[:36]:
        daily_cards += f"""
        <div class="article-card" data-art-search="{art['title'].lower()} {art['brand'].lower()} {art['category'].lower()} {art['profile_title'].lower()}">
          <div>
            <div style="font-size:0.78rem; font-weight:700; color:#334155; text-transform:uppercase; margin-bottom:6px;">
              {art['date']} &bull; {art['category']} &bull; {art['load_lbs']} lbs Capacity
            </div>
            <h3 style="font-size:1.12rem; margin-bottom:10px;">
              <a href="{BASE_URL}/reviews/{art['slug']}.html" style="color:#0f172a;">{art['title']}</a>
            </h3>
            <p style="font-size:0.9rem; color:#334155; margin-bottom:14px;">
              Calibrated for <strong>{art['height_label']}</strong> (Sit: {art['sit_desk']}\" / Stand: {art['stand_desk']}\") with {art['brand_tech']}.
            </p>
          </div>
          <div style="display:flex; gap:10px; flex-wrap:wrap;">
            <a class="btn-outline" href="{BASE_URL}/reviews/{art['slug']}.html">Read Full Review</a>
            <a class="btn-amazon" style="padding:9px 14px; font-size:0.86rem;" href="{art['affiliate_url']}" target="_blank" rel="nofollow sponsored noopener">Amazon Price</a>
          </div>
        </div>
        """

    sitemap_preview_links = ""
    for art in all_articles[:18]:
        sitemap_preview_links += f"""
        <li><a href="{BASE_URL}/reviews/{art['slug']}.html">{art['title']}</a> ({art['date']})</li>
        """

    faqs = [
        (
            "How do I calculate my ideal sitting and standing desk height?",
            "Your elbows should bend at a relaxed 90 to 100-degree angle with shoulders dropped and wrists flat on the keyboard. Using ANSI/BIFMA anthropometric ratios, multiply your total height in inches by 0.405 (plus shoe heel height) for seated desk height, and multiply by 0.625 (plus shoe or walking-pad deck height) for standing desk height."
        ),
        (
            "Why do 3-stage dual-motor standing desks matter for shorter and taller people?",
            "Standard 2-stage desks only travel from 28 inches to 46 inches—which is too tall for seated users under 5'7\" and too short for standing users over 6'2\" (or anyone using an under-desk walking pad). 3-stage telescoping columns travel from 22.8 inches up to 48.5+ inches with vastly superior front-to-back stability."
        ),
        (
            "How high and how far away should my computer monitor be placed?",
            "Position the top bezel of your display at or slightly below eye level so your gaze angles gently downward by 10 to 15 degrees. Place the screen at roughly 1.1x to 1.25x your monitor's diagonal size (about 24 to 36 inches away) to prevent neck strain and eye fatigue."
        ),
        (
            "How do I choose a VESA monitor arm weight capacity for a curved or ultrawide display?",
            "Check your monitor's panel-only weight (without the factory stand) and multiply by 1.25x for gas-spring safety headroom. Deep-curved 34-inch to 49-inch ultrawide monitors shift the center of gravity forward, requiring a heavy-duty reinforced tilt pivot rated for 30 to 42+ lbs."
        ),
        (
            "How much extra desk height do I need if I use an under-desk walking pad treadmill?",
            "Most slim under-desk walking pads have a deck height between 4.2 and 5.2 inches. Add your treadmill's deck thickness directly to your normal standing desk height—for example, a 5'10\" user normally stands at 44.5 inches, so with a walking pad they need a desk that reaches at least 49 inches."
        ),
        (
            "What is the best sit-to-stand ratio during an 8-hour workday?",
            "Ergonomics researchers recommend the 20-8-2 rhythm or alternating roughly 30 to 45 minutes of sitting with 15 to 20 minutes of standing on a contoured anti-fatigue mat, avoiding locking your knees for hours at a time."
        )
    ]

    faq_html = ""
    faq_entities = []
    for q, a in faqs:
        faq_html += f"""
        <details class="faq-item" open>
          <summary>{q}</summary>
          <p>{a}</p>
        </details>
        """
        faq_entities.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": a}
        })

    json_ld = [
        {
            "@context": "https://schema.org",
            "@type": "WebApplication",
            "name": "ErgoDeskCalc — Standing Desk Height, Chair Seat, Monitor Eye-Level & VESA Arm Load Calculator",
            "applicationCategory": "UtilitiesApplication",
            "operatingSystem": "All",
            "url": f"{BASE_URL}/index.html",
            "description": "Free interactive ergonomic workstation height calculator for sitting desk, standing desk, chair seat, monitor viewing distance, and VESA arm weight capacity."
        },
        {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": faq_entities
        }
    ]

    js_products = json.dumps([
        {
            "name": p["name"],
            "brand": p["brand"],
            "category": p["category"],
            "min_h_in": p["min_h_in"],
            "max_h_in": p["max_h_in"],
            "load_lbs": p["load_lbs"],
            "key_spec": p["key_spec"],
            "badge": p["badge"],
            "highlight": p["highlight"],
            "url": amazon_search_url(p["search_query"])
        }
        for p in CORE_PRODUCTS
    ])

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>ErgoDeskCalc — Standing Desk Height, Ergonomic Chair &amp; Monitor Arm Load Calculator</title>
  <meta name="description" content="Calculate exact seated desk height, standing desk height, chair seat height, monitor viewing distance, and VESA arm load capacity in seconds. Compare top ergonomic office gear &amp; daily reviews." />
  <link rel="canonical" href="{BASE_URL}/index.html" />
  <link rel="alternate" type="application/rss+xml" title="ErgoDeskCalc Daily Ergonomic Office Reviews RSS" href="{BASE_URL}/feed.xml" />
  <meta property="og:title" content="ErgoDeskCalc — Interactive Standing Desk, Chair &amp; Monitor Ergonomics Calculator" />
  <meta property="og:description" content="Dial in your exact desk height, chair seat height, and monitor arm load rating with instant hardware matches." />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="{BASE_URL}/index.html" />
  <style>{GLOBAL_CSS}</style>
  <script type="application/ld+json">{json.dumps(json_ld)}</script>
</head>
<body>

  <!-- TOP STICKY PROMO BANNER -->
  <div class="top-promo-banner">
    <span class="badge-live">HOME OFFICE DEALS</span>
    Save Up to 40% on FlexiSpot Dual-Motor Standing Desks, Ergotron Monitor Arms, Ergonomic Chairs &amp; Walking Pads
    <a class="banner-cta" href="{amazon_search_url('Dual Motor Standing Desk Ergonomic Chair Monitor Arm Deal')}" target="_blank" rel="nofollow sponsored noopener">Claim Today's Amazon Coupons &rarr;</a>
  </div>

  <!-- NAVIGATION HEADER -->
  <header class="site-header">
    <div class="container nav-flex">
      <a href="{BASE_URL}/index.html" class="brand-logo">ErgoDesk<span>Calc</span></a>
      <ul class="nav-links">
        <li><a href="#calculator">Ergonomic Calculator</a></li>
        <li><a href="#search-section">Search Products</a></li>
        <li><a href="#bestsellers">Best Sellers</a></li>
        <li><a href="#comparison">Comparison Chart</a></li>
        <li><a href="#daily-reviews">Daily Reviews ({len(all_articles)})</a></li>
        <li><a href="#faq">FAQ</a></li>
        <li><a href="#sitemap-section">Site Map</a></li>
      </ul>
    </div>
  </header>

  <main class="container">

    <!-- HERO BANNER -->
    <section class="hero-banner">
      <div class="hero-grid">
        <div>
          <h1>Standing Desk Height, Ergonomic Chair &amp; Monitor Arm Load Calculator</h1>
          <p>Eliminate neck strain, wrist pain, and desk wobble. Enter your height, footwear or walking-pad deck allowance, and monitor size below to compute your exact <strong>ANSI/BIFMA Seated &amp; Standing Desk Height</strong>, <strong>Chair Seat Height</strong>, <strong>Monitor Viewing Distance</strong>, and <strong>VESA Arm Weight Rating</strong>—paired with instant Amazon hardware matches.</p>
          <div style="display:flex; gap:12px; flex-wrap:wrap;">
            <a class="btn-amazon" href="#calculator">Launch Ergonomic Calculator &darr;</a>
            <a class="btn-outline" style="color:#ffffff; border-color:#94a3b8;" href="{amazon_search_url('Best Selling Standing Desk Ergonomic Office Chair')}" target="_blank" rel="nofollow sponsored noopener">Browse Amazon Office Best Sellers &rarr;</a>
          </div>
        </div>
        <div class="hero-deal-box">
          <h3>🖥️ Featured Workstation Upgrade</h3>
          <p style="color:#e2e8f0; font-size:0.92rem; margin-bottom:14px;">3-Stage Dual-Motor Standing Desks (22.8\"–48.4\"), Heavy-Duty Ultrawide Monitor Arms &amp; Walking Pads.</p>
          <a class="btn-amazon" style="width:100%;" href="{amazon_search_url('FlexiSpot E7 Standing Desk Ergotron LX Arm UREVO Walking Pad')}" target="_blank" rel="nofollow sponsored noopener">View Live Amazon Discounts &rarr;</a>
        </div>
      </div>
    </section>

    <!-- 4-IN-1 INTERACTIVE ERGONOMIC WORKSTATION CALCULATOR -->
    <section id="calculator" class="grey-section">
      <h2 class="section-title">Interactive 4-in-1 Standing Desk, Chair, Monitor Distance &amp; VESA Arm Calculator</h2>
      <p class="section-sub">Click a height preset or enter your exact measurements below. All outputs update instantly in both Inches and Centimeters (cm) with live equipment matching.</p>

      <div class="preset-row">
        <button type="button" class="preset-btn" onclick="setErgoPreset(5, 3, 0.8, 27, 13, 0)">👩 Petite User (5'3\" + 27\" Monitor)</button>
        <button type="button" class="preset-btn" onclick="setErgoPreset(5, 9, 1.0, 32, 18, 0)">🧑 Standard Setup (5'9\" + 32\" 4K)</button>
        <button type="button" class="preset-btn" onclick="setErgoPreset(6, 2, 1.0, 34, 22, 0)">👨 Tall User (6'2\" + 34\" Ultrawide)</button>
        <button type="button" class="preset-btn" onclick="setErgoPreset(5, 10, 1.0, 27, 14, 4.8)">🚶 Walking Pad Setup (5'10\" + 4.8\" Deck)</button>
        <button type="button" class="preset-btn" onclick="setErgoPreset(6, 0, 1.0, 49, 32, 0)">🎮 49\" Super-Ultrawide Battlestation</button>
      </div>

      <div class="calc-grid">
        <div class="calc-panel">
          <div class="form-row">
            <div class="form-group">
              <label for="ergoFt">1. Your Height (Feet):</label>
              <input type="number" id="ergoFt" value="5" min="4" max="7" oninput="calculateErgonomics()" />
            </div>
            <div class="form-group">
              <label for="ergoIn">2. Additional Inches (0–11):</label>
              <input type="number" id="ergoIn" value="10" min="0" max="11" oninput="calculateErgonomics()" />
            </div>
          </div>
          <div class="form-row">
            <div class="form-group">
              <label for="ergoHeel">3. Footwear / Standing Mat Elevation:</label>
              <select id="ergoHeel" onchange="calculateErgonomics()">
                <option value="0">Barefoot / Socks (0.0 in)</option>
                <option value="0.8">Indoor Slippers / Thin Mat (0.8 in)</option>
                <option value="1.0" selected>Sneakers / Cushioned Anti-Fatigue Mat (1.0 in)</option>
                <option value="1.5">Work Boots / Thick 3D Contoured Mat (1.5 in)</option>
              </select>
            </div>
            <div class="form-group">
              <label for="ergoWalkPad">4. Under-Desk Walking Pad Deck:</label>
              <select id="ergoWalkPad" onchange="calculateErgonomics()">
                <option value="0" selected>No Walking Pad (Standard Standing)</option>
                <option value="4.5">Slim Walking Pad (+4.5 in Standing Elevation)</option>
                <option value="5.2">Standard Treadmill Deck (+5.2 in Standing Elevation)</option>
              </select>
            </div>
          </div>
          <div class="form-row">
            <div class="form-group">
              <label for="ergoMonSize">5. Primary Monitor Diagonal (Inches):</label>
              <input type="number" id="ergoMonSize" value="27" min="15" max="57" oninput="calculateErgonomics()" />
            </div>
            <div class="form-group">
              <label for="ergoMonWeight">6. Monitor Panel Weight (lbs, w/o Stand):</label>
              <input type="number" id="ergoMonWeight" value="14" min="4" max="45" oninput="calculateErgonomics()" />
            </div>
          </div>
        </div>

        <div class="calc-panel">
          <h3 style="margin-bottom:12px; color:#0f172a;">Your Exact Ergonomic Workstation Specs</h3>
          <div class="metrics-grid">
            <div class="metric-card">
              <div class="val" id="outSitDesk">29.4\" (75 cm)</div>
              <div class="lbl">Seated Desk &amp; Keyboard Height</div>
            </div>
            <div class="metric-card">
              <div class="val" id="outStandDesk">44.8\" (114 cm)</div>
              <div class="lbl">Standing Desk Height</div>
            </div>
            <div class="metric-card">
              <div class="val" id="outChairSeat">18.5\" (47 cm)</div>
              <div class="lbl">Ergonomic Chair Seat Height</div>
            </div>
            <div class="metric-card">
              <div class="val" id="outMonitorDist">31\" | 18+ lb Arm</div>
              <div class="lbl">Viewing Distance &amp; Min. VESA Arm</div>
            </div>
          </div>

          <div id="dynamicErgoRec" class="rec-box">
            <!-- Dynamically populated by JS -->
          </div>
        </div>
      </div>
    </section>

    <!-- PRODUCT SEARCH & FILTER -->
    <section id="search-section" class="grey-section">
      <h2 class="section-title">Search Amazon Standing Desks, Monitor Arms, Chairs &amp; Walking Pads</h2>
      <p class="section-sub">Filter our verified catalog and daily review archive by brand, keyword, or category, or search directly on Amazon.</p>
      <div class="search-bar">
        <input type="text" id="ergoSearchInput" class="search-input" placeholder="Search FlexiSpot, Ergotron, Steelcase, SIHOO, ultrawide, dual motor, walking pad..." oninput="filterErgoCatalog()" />
        <select id="ergoCatSelect" class="filter-select" onchange="filterErgoCatalog()">
          <option value="ALL">All Office Categories</option>
          <option value="Standing Desk">Electric Standing Desks</option>
          <option value="Monitor Arm">VESA Monitor Arms</option>
          <option value="Ergonomic Chair">Ergonomic Task Chairs</option>
          <option value="Standing Accessories">Walking Pads &amp; Standing Mats</option>
          <option value="Ergonomic Peripherals">Split Keyboards &amp; Vertical Mice</option>
        </select>
        <button type="button" class="btn-amazon" onclick="searchErgoAmazonDirect()">Search Live on Amazon &rarr;</button>
      </div>
      <p id="ergoFilterStatus" style="font-size:0.88rem; font-weight:700; color:#334155;">Showing all 10 top-rated ergonomic workstation products below:</p>
    </section>

    <!-- BEST SELLERS -->
    <section id="bestsellers" class="grey-section">
      <h2 class="section-title">Best-Selling Standing Desks, Monitor Arms, Chairs &amp; Walking Pads</h2>
      <p class="section-sub">Ranked by BIFMA structural stability, height adjustability range, load capacity, and verified Amazon buyer satisfaction.</p>
      <div id="ergoBestSellersGrid" class="product-grid">
        {bestsellers_cards}
      </div>
    </section>

    <!-- COMPARISON TABLE -->
    <section id="comparison" class="grey-section">
      <h2 class="section-title">Side-by-Side Ergonomic Gear Comparison Matrix</h2>
      <p class="section-sub">Compare minimum/maximum height travel, load capacity, key mechanism, and ergonomic advantage across flagship models.</p>
      <div class="table-wrap">
        <table class="comp-table">
          <thead>
            <tr>
              <th>Product Model</th>
              <th>Category</th>
              <th>Height / Lift Range</th>
              <th>Max Load</th>
              <th>Hardware Mechanism</th>
              <th>Ergonomic Benefit</th>
              <th>Rating</th>
              <th>Amazon Deal</th>
            </tr>
          </thead>
          <tbody>
            {comparison_rows}
          </tbody>
        </table>
      </div>
    </section>

    <!-- DAILY AUTOMATED PRODUCT REVIEWS -->
    <section id="daily-reviews" class="grey-section">
      <h2 class="section-title">Daily Automated Ergonomic Product Reviews &amp; Fit Tests</h2>
      <p class="section-sub">Our automated GitHub Actions pipeline publishes <strong>3 brand-new ergonomic office product reviews every single day</strong>. Browse the latest reviews below (Total live articles: <strong>{len(all_articles)}</strong>):</p>
      <div id="dailyErgoReviewsGrid" class="articles-grid">
        {daily_cards}
      </div>
    </section>

    <!-- FAQ SECTION -->
    <section id="faq" class="grey-section">
      <h2 class="section-title">Frequently Asked Questions (Desk Height, Monitor Distance &amp; Chair Fit)</h2>
      <p class="section-sub">Essential OSHA and ANSI/BIFMA workstation ergonomics formulas explained clearly.</p>
      {faq_html}
    </section>

    <!-- ON-PAGE SITE MAP DIRECTORY -->
    <section id="sitemap-section" class="grey-section">
      <h2 class="section-title">Site Map &amp; Complete Content Directory</h2>
      <p class="section-sub">Direct navigation for visitors and search engine crawlers across all calculators, feeds, and daily review archives.</p>
      <div class="sitemap-columns">
        <div class="sitemap-box">
          <h3>Main Tools &amp; XML Feeds</h3>
          <ul>
            <li><a href="#calculator">4-in-1 Standing Desk, Chair &amp; Monitor Arm Calculator</a></li>
            <li><a href="#bestsellers">Top 10 Best-Selling Ergonomic Office Products</a></li>
            <li><a href="#comparison">Side-by-Side Comparison Matrix</a></li>
            <li><a href="{BASE_URL}/sitemap.html"><strong>Full HTML Site Map Page (All {len(all_articles)} Reviews)</strong></a></li>
            <li><a href="{BASE_URL}/sitemap.xml">Google/Bing XML Sitemap (sitemap.xml)</a></li>
            <li><a href="{BASE_URL}/feed.xml">RSS 2.0 Syndication Feed (feed.xml)</a></li>
          </ul>
        </div>
        <div class="sitemap-box">
          <h3>Latest Daily Ergonomic Review Archive Links</h3>
          <ul>
            {sitemap_preview_links}
          </ul>
        </div>
      </div>
    </section>

  </main>

  <footer class="site-footer">
    <div class="container">
      <div class="footer-links">
        <a href="#calculator">Ergonomic Calculator</a>
        <a href="#search-section">Product Search</a>
        <a href="#bestsellers">Best Sellers</a>
        <a href="#comparison">Comparison Table</a>
        <a href="#daily-reviews">Daily Reviews</a>
        <a href="#faq">FAQ</a>
        <a href="{BASE_URL}/sitemap.html">HTML Site Map</a>
        <a href="{BASE_URL}/sitemap.xml">XML Sitemap</a>
        <a href="{BASE_URL}/feed.xml">RSS Feed</a>
      </div>
      <p style="margin-bottom:8px;"><strong>Amazon Affiliate Disclosure:</strong> ErgoDeskCalc participates in the Amazon Services LLC Associates Program (Affiliate StoreID: <code>{AFFILIATE_TAG}</code>), an affiliate advertising program designed to provide a means for sites to earn advertising fees by linking to Amazon.com.</p>
      <p>&copy; {datetime.datetime.now(datetime.timezone.utc).year} ErgoDeskCalc. Powered by zero-maintenance GitHub Actions automation.</p>
    </div>
  </footer>

  <script>
    var ERGO_PRODUCTS = {js_products};
    var AFFILIATE_TAG = "{AFFILIATE_TAG}";

    function setErgoPreset(ft, inch, heel, monSize, monWt, walkPad) {{
      document.getElementById('ergoFt').value = ft;
      document.getElementById('ergoIn').value = inch;
      document.getElementById('ergoHeel').value = heel.toString();
      document.getElementById('ergoMonSize').value = monSize;
      document.getElementById('ergoMonWeight').value = monWt;
      document.getElementById('ergoWalkPad').value = walkPad.toString();
      calculateErgonomics();
    }}

    function calculateErgonomics() {{
      var ft = parseFloat(document.getElementById('ergoFt').value) || 5;
      var inch = parseFloat(document.getElementById('ergoIn').value) || 10;
      var heel = parseFloat(document.getElementById('ergoHeel').value) || 1.0;
      var walkPad = parseFloat(document.getElementById('ergoWalkPad').value) || 0;
      var monSize = parseFloat(document.getElementById('ergoMonSize').value) || 27;
      var monWt = parseFloat(document.getElementById('ergoMonWeight').value) || 14;

      var totalIn = (ft * 12) + inch;
      var sitDesk = +(totalIn * 0.405 + heel).toFixed(1);
      var standDesk = +(totalIn * 0.625 + heel + walkPad).toFixed(1);
      var chairSeat = +(totalIn * 0.25 + heel).toFixed(1);

      var viewDist = Math.round(Math.min(42, Math.max(20, monSize * 1.15)));
      var minArmLoad = Math.ceil(monWt * 1.25);

      document.getElementById('outSitDesk').textContent = sitDesk + '\" (' + Math.round(sitDesk * 2.54) + ' cm)';
      document.getElementById('outStandDesk').textContent = standDesk + '\" (' + Math.round(standDesk * 2.54) + ' cm)';
      document.getElementById('outChairSeat').textContent = chairSeat + '\" (' + Math.round(chairSeat * 2.54) + ' cm)';
      document.getElementById('outMonitorDist').textContent = viewDist + '\" Dist | ' + minArmLoad + '+ lb Arm';

      // Find best standing desk covering both seated and standing calculated heights
      var desks = ERGO_PRODUCTS.filter(function(p) {{ return p.category === 'Standing Desk'; }});
      var bestDesk = desks.find(function(d) {{ return d.min_h_in <= sitDesk && d.max_h_in >= standDesk; }}) || desks[0];

      // Find best monitor arm handling monitor weight with 25% safety margin
      var arms = ERGO_PRODUCTS.filter(function(p) {{ return p.category === 'Monitor Arm'; }})
        .sort(function(a, b) {{ return a.load_lbs - b.load_lbs; }});
      var bestArm = arms.find(function(a) {{ return a.load_lbs >= minArmLoad; }}) || arms[arms.length - 1];

      var customDeskUrl = 'https://www.amazon.com/s?k=' + encodeURIComponent('3 stage dual motor standing desk ' + Math.ceil(standDesk) + ' inch height') + '&tag=' + AFFILIATE_TAG;
      var customArmUrl = 'https://www.amazon.com/s?k=' + encodeURIComponent('heavy duty monitor arm ' + monSize + ' inch ' + minArmLoad + ' lbs') + '&tag=' + AFFILIATE_TAG;
      var chairUrl = 'https://www.amazon.com/s?k=' + encodeURIComponent('ergonomic office chair adjustable lumbar seat height') + '&tag=' + AFFILIATE_TAG;

      var html = '<h4>✅ Matched Hardware for Your ' + ft + '\\'' + inch + '\" Ergonomic Profile:</h4>' +
        '<p style="font-size:0.9rem; color:#334155; margin-bottom:10px;"><strong>Desk Match:</strong> ' + bestDesk.name + ' (' + bestDesk.min_h_in + '\"–' + bestDesk.max_h_in + '\") &bull; <strong>VESA Arm Match:</strong> ' + bestArm.name + ' (up to ' + bestArm.load_lbs + ' lbs).</p>' +
        '<div style="display:flex; gap:8px; flex-wrap:wrap;">' +
        '<a class="btn-amazon" href="' + bestDesk.url + '" target="_blank" rel="nofollow sponsored noopener">Check ' + bestDesk.brand + ' Desk on Amazon &rarr;</a>' +
        '<a class="btn-outline" href="' + bestArm.url + '" target="_blank" rel="nofollow sponsored noopener">Check ' + bestArm.brand + ' Monitor Arm</a>' +
        '<a class="btn-outline" href="' + customDeskUrl + '" target="_blank" rel="nofollow sponsored noopener">Shop ' + Math.ceil(standDesk) + '\"+ Standing Desks</a>' +
        '<a class="btn-outline" href="' + chairUrl + '" target="_blank" rel="nofollow sponsored noopener">Shop Ergonomic Chairs</a>' +
        '</div>';

      document.getElementById('dynamicErgoRec').innerHTML = html;
    }}

    function filterErgoCatalog() {{
      var q = (document.getElementById('ergoSearchInput').value || '').toLowerCase().trim();
      var cat = document.getElementById('ergoCatSelect').value;
      var cards = document.querySelectorAll('#ergoBestSellersGrid .product-card');
      var shown = 0;

      cards.forEach(function(c) {{
        var s = c.getAttribute('data-search') || '';
        var cCat = c.getAttribute('data-category') || '';
        var okQ = !q || s.indexOf(q) !== -1;
        var okC = (cat === 'ALL') || (cCat === cat);
        if (okQ && okC) {{
          c.style.display = 'flex';
          shown++;
        }} else {{
          c.style.display = 'none';
        }}
      }});

      var artCards = document.querySelectorAll('#dailyErgoReviewsGrid .article-card');
      artCards.forEach(function(ac) {{
        var aSearch = ac.getAttribute('data-art-search') || '';
        ac.style.display = (!q || aSearch.indexOf(q) !== -1) ? 'flex' : 'none';
      }});

      document.getElementById('ergoFilterStatus').textContent =
        'Showing ' + shown + ' matching flagship product(s) (and filtered daily review articles below):';
    }}

    function searchErgoAmazonDirect() {{
      var q = document.getElementById('ergoSearchInput').value.trim() || 'Dual Motor Standing Desk Ergonomic Chair Monitor Arm';
      window.open('https://www.amazon.com/s?k=' + encodeURIComponent(q) + '&tag=' + AFFILIATE_TAG, '_blank');
    }}

    calculateErgonomics();
  </script>
</body>
</html>"""


def generate_sitemaps_and_feeds(all_articles: list[dict]) -> list[str]:
    """Menghasilkan sitemap.xml, sitemap.html, robots.txt, feed.xml, dan kunci verifikasi IndexNow."""
    today_iso = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
    urls = [f"{BASE_URL}/index.html", f"{BASE_URL}/sitemap.html"]

    sitemap_entries = f"""  <url>
    <loc>{BASE_URL}/index.html</loc>
    <lastmod>{today_iso}</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>{BASE_URL}/sitemap.html</loc>
    <lastmod>{today_iso}</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.9</priority>
  </url>\n"""

    for art in all_articles:
        u = f"{BASE_URL}/reviews/{art['slug']}.html"
        urls.append(u)
        sitemap_entries += f"""  <url>
    <loc>{u}</loc>
    <lastmod>{art['date']}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>\n"""

    sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{sitemap_entries}</urlset>"""

    with open(os.path.join(OUTPUT_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sitemap_xml)

    # HTML Site Map Page (sitemap.html)
    html_sitemap = build_html_sitemap_page(all_articles)
    with open(os.path.join(OUTPUT_DIR, "sitemap.html"), "w", encoding="utf-8") as f:
        f.write(html_sitemap)

    # robots.txt
    robots_txt = f"""User-agent: *
Allow: /

Sitemap: {BASE_URL}/sitemap.xml
"""
    with open(os.path.join(OUTPUT_DIR, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(robots_txt)

    # RSS 2.0 Feed (feed.xml)
    rss_items = ""
    for art in all_articles[:30]:
        u = f"{BASE_URL}/reviews/{art['slug']}.html"
        rss_items += f"""    <item>
      <title><![CDATA[{art['title']}]]></title>
      <link>{u}</link>
      <guid>{u}</guid>
      <pubDate>{art['date']}T04:00:00Z</pubDate>
      <description><![CDATA[Ergonomic fit test and height calibration for {art['brand']} {art['model_name']} ({art['load_lbs']} lbs capacity) tailored to {art['profile_title']}.]]></description>
    </item>\n"""

    rss_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>ErgoDeskCalc — Daily Standing Desk, Chair &amp; Monitor Arm Reviews</title>
    <link>{BASE_URL}/index.html</link>
    <description>Automated daily ergonomic home office reviews and workstation height calculators.</description>
    <language>en-us</language>
{rss_items}  </channel>
</rss>"""

    with open(os.path.join(OUTPUT_DIR, "feed.xml"), "w", encoding="utf-8") as f:
        f.write(rss_xml)

    # IndexNow key verification file
    with open(os.path.join(OUTPUT_DIR, f"{INDEXNOW_KEY}.txt"), "w", encoding="utf-8") as f:
        f.write(INDEXNOW_KEY)

    return urls


def ping_indexnow(newly_added: list[dict]):
    """Mengirimkan ping otomatis ke IndexNow API agar mesin pencari langsung mengindeks 3 artikel baru setiap hari."""
    host = urllib.parse.urlparse(BASE_URL).netloc
    url_list = [
        f"{BASE_URL}/index.html",
        f"{BASE_URL}/sitemap.html",
        f"{BASE_URL}/sitemap.xml"
    ]
    for art in newly_added:
        url_list.append(f"{BASE_URL}/reviews/{art['slug']}.html")

    payload = json.dumps({
        "host": host,
        "key": INDEXNOW_KEY,
        "keyLocation": f"{BASE_URL}/{INDEXNOW_KEY}.txt",
        "urlList": url_list
    }).encode("utf-8")

    req = urllib.request.Request(
        "https://api.indexnow.org/indexnow",
        data=payload,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            print(f"[IndexNow] Pinged {len(url_list)} URLs successfully (HTTP {resp.status})")
    except Exception as exc:
        print(f"[IndexNow] Notice (non-blocking): {exc}")


def main():
    os.makedirs(REVIEWS_DIR, exist_ok=True)
    all_articles, newly_added = load_and_advance_state()

    # 1. Build Homepage
    index_html = build_index_page(all_articles)
    with open(os.path.join(OUTPUT_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_html)

    # 2. Build Individual Review Pages
    for art in all_articles:
        page_html = build_article_page(art, all_articles)
        out_path = os.path.join(REVIEWS_DIR, f"{art['slug']}.html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(page_html)

    # 3. Build Sitemap XML, Sitemap HTML, Robots.txt, RSS Feed & Ping IndexNow
    generate_sitemaps_and_feeds(all_articles)
    ping_indexnow(newly_added)

    print(f"ErgoDeskCalc build finished! Total articles live: {len(all_articles)} (+{len(newly_added)} added today).")


if __name__ == "__main__":
    main()
