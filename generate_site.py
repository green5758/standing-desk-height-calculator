#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SoilBagCalc - Garden Soil, Mulch, Compost & Raised Bed Volume Calculator
+ Automated Daily Amazon Product Review Publisher
Affiliate StoreID: everythi00099-20
"""

import os
import json
import math
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

REPO_FULL = os.environ.get("GITHUB_REPOSITORY", "username/soilbagcalc")
REPO_OWNER = os.environ.get("GITHUB_REPOSITORY_OWNER", REPO_FULL.split("/")[0])
REPO_NAME = REPO_FULL.split("/")[-1] if "/" in REPO_FULL else "soilbagcalc"

if REPO_NAME.lower() == f"{REPO_OWNER.lower()}.github.io":
    BASE_URL = f"https://{REPO_OWNER.lower()}.github.io"
else:
    BASE_URL = f"https://{REPO_OWNER.lower()}.github.io/{REPO_NAME}"

INDEXNOW_KEY = hashlib.md5(f"soilbagcalc-{AFFILIATE_TAG}".encode("utf-8")).hexdigest()


def amazon_search_url(query: str) -> str:
    encoded = urllib.parse.quote_plus(query)
    return f"https://www.amazon.com/s?k={encoded}&tag={AFFILIATE_TAG}"


# ==============================================================================
# MASTER BEST SELLER & COMPARISON CATALOG (10 FLAGSHIP GARDEN SOIL & BED PRODUCTS)
# ==============================================================================
CORE_PRODUCTS = [
    {
        "id": "fox-farm-ocean-forest-potting-soil",
        "name": "FoxFarm FX14053 Ocean Forest Organic Potting Soil (12-Quart / 2 Cu.Ft.)",
        "brand": "FoxFarm",
        "category": "Potting & Raised Bed Soil",
        "bag_cuft": 2.0,
        "coverage_at_3in_sqft": 8.0,
        "soil_type": "Aged Forest Humus, Earthworm Castings & Bat Guano",
        "ph_range": "6.3 – 6.8 pH (Ready to Plant)",
        "rating": "4.7",
        "reviews_count": 26400,
        "badge": "#1 Best Selling Potting Soil",
        "search_query": "FoxFarm Ocean Forest Organic Potting Soil",
        "highlight": "Pre-charged with composted forest humus, peat moss, earthworm castings, fish emulsion, and sandy loam for vigorous root aeration."
    },
    {
        "id": "miracle-gro-raised-bed-soil",
        "name": "Miracle-Gro Raised Bed Soil Blended for Vegetables, Herbs & Flowers",
        "brand": "Miracle-Gro",
        "category": "Potting & Raised Bed Soil",
        "bag_cuft": 2.0,
        "coverage_at_3in_sqft": 8.0,
        "soil_type": "Compost, Peat Moss & Slow-Release Plant Food",
        "ph_range": "6.0 – 7.0 pH (Feeds up to 3 Months)",
        "rating": "4.6",
        "reviews_count": 18900,
        "badge": "Best Raised Bed Mix",
        "search_query": "Miracle-Gro Raised Bed Soil Vegetables Flowers",
        "highlight": "Formulated specifically not to compact in raised wooden or metal beds while feeding tomatoes, peppers, and greens for up to 3 months."
    },
    {
        "id": "vivosun-heavy-duty-fabric-grow-bags",
        "name": "VIVOSUN 5-Pack 10-Gallon Heavy-Duty 300G Nonwoven Fabric Grow Pots",
        "brand": "VIVOSUN",
        "category": "Fabric Grow Bags",
        "bag_cuft": 1.34,
        "coverage_at_3in_sqft": 12.5,
        "soil_type": "300g Thickened Breathable Nonwoven Geotextile",
        "ph_range": "Air-Prunes Roots & Prevents Overwatering",
        "rating": "4.7",
        "reviews_count": 39200,
        "badge": "#1 Best Selling Grow Bags",
        "search_query": "VIVOSUN Heavy Duty Fabric Grow Bags 10 Gallon",
        "highlight": "Reinforced stitched handles and breathable fabric walls promote fibrous root air-pruning and superior drainage on patios or decks."
    },
    {
        "id": "vegega-galvanized-raised-garden-bed",
        "name": "VEGEGA 8x2x1.5 ft 9-in-1 Modular Galvanized Metal Raised Garden Bed",
        "brand": "VEGEGA",
        "category": "Metal Raised Garden Beds",
        "bag_cuft": 24.0,
        "coverage_at_3in_sqft": 16.0,
        "soil_type": "Aluzinc Corrosion-Resistant Steel (0.8mm–1.8mm)",
        "ph_range": "Eco-Friendly Non-Leaching Coating",
        "rating": "4.6",
        "reviews_count": 5840,
        "badge": "Best Deep Raised Bed",
        "search_query": "VEGEGA Galvanized Metal Raised Garden Bed",
        "highlight": "17-inch tall wall height supports deep root crops and hugelkultur bottom-fill layering while resisting rust for 20+ years."
    },
    {
        "id": "scott-naturals-cedar-mulch",
        "name": "Scotts Nature Scapes 2 Cu. Ft. Deep Forest Brown Color-Enhanced Mulch",
        "brand": "Scotts",
        "category": "Garden Mulch & Compost",
        "bag_cuft": 2.0,
        "coverage_at_3in_sqft": 8.0,
        "soil_type": "100% Recycled Forest Wood Fiber (1-Year Color Lock)",
        "ph_range": "Suppresses Weeds & Retains Soil Moisture",
        "rating": "4.6",
        "reviews_count": 11300,
        "badge": "#1 Best Selling Mulch",
        "search_query": "Scotts Nature Scapes Mulch 2 cu ft",
        "highlight": "Locks in soil moisture during hot summer weeks and blocks annual weed germination around shrubs, trees, and perennial borders."
    },
    {
        "id": "coast-of-maine-stonington-blend",
        "name": "Coast of Maine Stonington Blend Organic Grower's Mix (1 Cu. Ft.)",
        "brand": "Coast of Maine",
        "category": "Potting & Raised Bed Soil",
        "bag_cuft": 1.0,
        "coverage_at_3in_sqft": 4.0,
        "soil_type": "Lobster & Crab Compost, Sphagnum Peat & Kelp Meal",
        "ph_range": "6.2 – 6.8 pH (OMRI Listed Organic)",
        "rating": "4.7",
        "reviews_count": 4720,
        "badge": "Top Organic Grower Mix",
        "search_query": "Coast of Maine Stonington Blend Organic Grower Mix",
        "highlight": "Rich marine compost and kelp meal blend with balanced water retention and drainage for heirloom vegetables and containers."
    },
    {
        "id": "black-kow-composted-cow-manure",
        "name": "Black Kow 50-lb (1 Cu. Ft.) Composted Cow Manure Soil Amendment",
        "brand": "Black Kow",
        "category": "Garden Mulch & Compost",
        "bag_cuft": 1.0,
        "coverage_at_3in_sqft": 4.0,
        "soil_type": "100% Composted Cow Manure + Lime & Humus",
        "ph_range": "Odor-Free Aged Organic Microbe Booster",
        "rating": "4.7",
        "reviews_count": 15600,
        "badge": "Best Soil Conditioner",
        "search_query": "Black Kow Composted Cow Manure 50 lb",
        "highlight": "Improves clay and sandy native soil structure by blending 25%–50% composted organic matter into existing garden beds."
    },
    {
        "id": "ac-infinity-heavy-duty-grow-bags",
        "name": "AC Infinity 4-Pack 5-Gallon Heavy-Duty 500G Fabric Grow Bags",
        "brand": "AC Infinity",
        "category": "Fabric Grow Bags",
        "bag_cuft": 0.67,
        "coverage_at_3in_sqft": 8.0,
        "soil_type": "Ultra-Thick 500G Woven Fabric + Nylon Straps",
        "ph_range": "High-Drainage Root Zone Aeration",
        "rating": "4.8",
        "reviews_count": 8910,
        "badge": "Heavy-Duty 500G Fabric",
        "search_query": "AC Infinity Heavy Duty 5 Gallon Fabric Grow Bags",
        "highlight": "Heavy 500gsm fabric resists tearing when moving loaded pots and keeps root temperatures cooler in direct afternoon sun."
    },
    {
        "id": "vivosun-galvanized-raised-bed-oval",
        "name": "VIVOSUN 6x3x1 ft Oval Galvanized Steel Raised Garden Bed Kit",
        "brand": "VIVOSUN",
        "category": "Metal Raised Garden Beds",
        "bag_cuft": 18.0,
        "coverage_at_3in_sqft": 18.0,
        "soil_type": "Double-Layer Anti-Rust Galvanized Sheet Steel",
        "ph_range": "Open-Bottom Drainage + Rubber Edge Trim",
        "rating": "4.6",
        "reviews_count": 12800,
        "badge": "Best Value Metal Bed",
        "search_query": "VIVOSUN Galvanized Raised Garden Bed 6x3x1 ft",
        "highlight": "Tool-friendly bolt assembly with protective top edge strip and open bottom for natural earthworm migration and drainage."
    },
    {
        "id": "back-to-the-roots-organic-seed-starter",
        "name": "Back to the Roots 100% Organic Potting Mix & Seed Starting Blend",
        "brand": "Back to the Roots",
        "category": "Potting & Raised Bed Soil",
        "bag_cuft": 1.5,
        "coverage_at_3in_sqft": 6.0,
        "soil_type": "Peat-Free / Sustainable Coir, Compost & Perlite",
        "ph_range": "6.2 – 6.8 pH (Peat-Free Option)",
        "rating": "4.5",
        "reviews_count": 6430,
        "badge": "Best Peat-Free Blend",
        "search_query": "Back to the Roots Organic Potting Mix",
        "highlight": "Lightweight organic blend with yucca extract wetting agent for even moisture distribution across indoor planters and outdoor beds."
    }
]


# ==============================================================================
# COMBINATORIAL ENGINE FOR 1,800 UNIQUE DAILY GARDEN SOIL & BED REVIEWS
# ==============================================================================
BRANDS_MATRIX = [
    ("FoxFarm", "Aged Forest Humus, Earthworm Castings & Balanced Drainage"),
    ("Miracle-Gro", "Controlled-Release Plant Nutrition & Loose Root Aeration"),
    ("Coast of Maine", "Marine Kelp Meal, Lobster Compost & OMRI Organic Matter"),
    ("Black Kow", "Aged Composted Cow Manure & Beneficial Soil Microbes"),
    ("VIVOSUN", "Breathable Nonwoven Root Fabric & Anti-Rust Galvanized Panels"),
    ("VEGEGA", "Heavy-Gauge Aluzinc Steel & Modular Multi-Shape Bed Framing"),
    ("Scotts", "Color-Lock Forest Mulch Fiber & Moisture-Retaining Texture"),
    ("AC Infinity", "500G Heavy-Duty Woven Geotextile & Reinforced Load Handles"),
    ("Back to the Roots", "Sustainable Organic Compost Blend & Even Wetting Matrix"),
    ("Espoma Organic", "Mycorrhizae Root Enhancer & Natural Compost Humate"),
    ("Happy Frog", "Soil Conditioner with Beneficial Fungi & Humic Acids"),
    ("Gardzen", "Heavy-Duty Breathable Aeration Pots & Drainage Reinforcement"),
    ("Keter", "Weather-Resistant Resin Planter Wall & Wood-Grain Finish"),
    ("LifeSmart", "UV-Stabilized Composite Garden Edging & Modular Bed Kit"),
    ("Burpee", "Eco-Friendly Seed & Root Blend with High Perlite Porosity"),
]

MODELS_MATRIX = [
    ("2 Cu. Ft. Organic Raised Bed & Potting Soil Bag", 2.0, 8.0, "Potting & Raised Bed Soil", "6.3–6.8 pH", "Loose Loam & Compost"),
    ("1.5 Cu. Ft. Premium Container & Planter Mix", 1.5, 6.0, "Potting & Raised Bed Soil", "6.2–6.7 pH", "High-Perlite Aeration Mix"),
    ("1 Cu. Ft. (50 lb) Composted Manure Soil Amendment", 1.0, 4.0, "Garden Mulch & Compost", "Neutral pH", "Rich Organic Humus"),
    ("2 Cu. Ft. Deep Forest Hardwood & Bark Mulch", 2.0, 8.0, "Garden Mulch & Compost", "Weed & Moisture Barrier", "Shredded Bark & Wood Fiber"),
    ("8x2x1.5 ft (24 Cu. Ft.) Deep Metal Raised Garden Bed", 24.0, 16.0, "Metal Raised Garden Beds", "18-Inch Root Depth", "Galvanized Corrugated Steel"),
    ("6x3x1 ft (18 Cu. Ft.) Oval Galvanized Raised Bed", 18.0, 18.0, "Metal Raised Garden Beds", "12-Inch Wall Height", "Anti-Rust Coated Steel"),
    ("4x4x1 ft (16 Cu. Ft.) Square Kitchen Garden Bed", 16.0, 16.0, "Metal Raised Garden Beds", "12-Inch Wall Height", "Modular Corner Panels"),
    ("5-Pack 10-Gallon Heavy-Duty Breathable Grow Bags", 6.7, 15.0, "Fabric Grow Bags", "Air-Pruning Walls", "Thick Nonwoven Geotextile"),
    ("5-Pack 7-Gallon Tomato, Pepper & Potato Grow Pots", 4.7, 12.0, "Fabric Grow Bags", "High Drainage Rate", "Reinforced Strap Fabric"),
    ("4-Pack 15-Gallon Large Shrub & Patio Grow Bags", 8.0, 20.0, "Fabric Grow Bags", "Deep Root Volume", "Heavy-Duty Aeration Cloth"),
    ("3 Cu. Ft. Bulk-Equivalent Garden Soil Value Pack", 3.0, 12.0, "Potting & Raised Bed Soil", "6.2–6.8 pH", "Compost & Screened Topsoil"),
    ("2 Cu. Ft. Cedar & Cypress Landscape Mulch Bag", 2.0, 8.0, "Garden Mulch & Compost", "Natural Aromatic Fiber", "Moisture-Locking Mulch"),
]

APPLICATIONS_MATRIX = [
    ("8x4 ft Raised Vegetable Bed at 9-Inch Soil Depth (24 Cu. Ft.)", 24.0, "fills a classic 8x4 ft raised bed cleanly without running short mid-project"),
    ("4x8 ft Herb, Salad Green & Root Crop Planter (16 Cu. Ft.)", 16.0, "provides loose, clod-free root media for carrots, radishes, lettuce, and basil"),
    ("Backyard Shrub Border & Tree Ring Mulching at 3-Inch Depth", 18.0, "locks in moisture, moderates soil temperature swings, and suppresses weeds"),
    ("Sunny Patio, Deck & Balcony Container Garden Setup", 10.0, "delivers balanced drainage and aeration for tomatoes, peppers, and patio herbs"),
    ("Heavy Clay Yard Soil Remediation & Organic Matter Tilling", 20.0, "loosens dense clay structure when blended 1:3 with native backyard soil"),
    ("Deep-Rooted Raised Bed for Tomatoes, Zucchini & Peppers", 27.0, "supports deep taproots and moisture consistency during peak summer heat"),
    ("Pollinator Flower Bed & Perennial Border Refresh", 14.0, "creates a nutrient-rich bed for coneflowers, lavender, zinnias, and perennials"),
    ("Small Urban Backyard & Rental Yard Modular Bed Project", 12.0, "makes it easy to grow fresh produce in tight spaces without tearing up turf"),
    ("Walkway & Fence-Line Weed Suppression Mulch Strip", 15.0, "keeps narrow side-yard strips tidy with minimal seasonal maintenance"),
    ("Multi-Bed Kitchen Garden Expansion (Two 6x3 ft Beds)", 36.0, "scales efficiently across multiple raised beds while keeping bag math simple"),
]


def get_article_blueprint(index: int) -> dict:
    """Secara deterministik menghasilkan artikel review tanah/mulsa/bed kebun unik berdasarkan indeks."""
    b_idx = index % len(BRANDS_MATRIX)
    m_idx = (index // len(BRANDS_MATRIX)) % len(MODELS_MATRIX)
    a_idx = (index // (len(BRANDS_MATRIX) * len(MODELS_MATRIX))) % len(APPLICATIONS_MATRIX)

    brand_name, brand_tech = BRANDS_MATRIX[b_idx]
    model_name, vol_cuft, cov_3in, category, spec_note, media_type = MODELS_MATRIX[m_idx]
    app_title, target_cuft, app_benefit = APPLICATIONS_MATRIX[a_idx]

    bags_needed = max(1, math.ceil(target_cuft / max(vol_cuft, 0.5)))
    cu_yards = round(target_cuft / 27.0, 2)

    slug = f"review-{brand_name.lower().replace(' ', '-')}-{model_name.lower().replace('.', '').replace('/', '').replace(' ', '-')}-{index + 1}"
    slug = "".join(c if c.isalnum() or c == "-" else "" for c in slug)
    while "--" in slug:
        slug = slug.replace("--", "-")

    title = f"{brand_name} {model_name} Review: Sized for {app_title}"
    search_q = f"{brand_name} {model_name}"

    return {
        "index": index,
        "slug": slug,
        "title": title,
        "brand": brand_name,
        "brand_tech": brand_tech,
        "model_name": model_name,
        "category": category,
        "vol_cuft": vol_cuft,
        "cov_3in": cov_3in,
        "spec_note": spec_note,
        "media_type": media_type,
        "app_title": app_title,
        "target_cuft": target_cuft,
        "cu_yards": cu_yards,
        "bags_needed": bags_needed,
        "app_benefit": app_benefit,
        "rating": "4.8" if (index % 2 == 0) else "4.7",
        "search_query": search_q,
        "affiliate_url": amazon_search_url(search_q),
    }


def load_and_advance_state() -> tuple[list[dict], list[dict]]:
    """Memuat posts_state.json dan menambahkan 3 artikel review baru setiap hari."""
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
        count_to_add = 6
    else:
        count_to_add = DAILY_NEW_ARTICLES

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
# SHARED CSS — GREY BACKGROUND THEME
# ==============================================================================
GLOBAL_CSS = """
:root {
  --bg-page: #cbd5e1;
  --bg-section: #e2e8f0;
  --bg-card: #f1f5f9;
  --bg-dark: #1e293b;
  --bg-darker: #0f172a;
  --border-grey: #94a3b8;
  --text-main: #0f172a;
  --text-muted: #334155;
  --accent-amazon: #ff9900;
  --accent-green: #15803d;
  --accent-link: #0369a1;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  background-color: var(--bg-page);
  color: var(--text-main);
  line-height: 1.6;
}
a { color: var(--accent-link); text-decoration: none; }
.container { max-width: 1240px; margin: 0 auto; padding: 0 18px; }

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
  background: #4ade80;
  color: #052e16;
  font-weight: 800;
  padding: 4px 14px;
  border-radius: 5px;
}

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

.hero-banner {
  background: linear-gradient(135deg, #334155 0%, #1e293b 100%);
  color: #f8fafc;
  padding: 34px 26px;
  margin: 24px 0;
  border-radius: 12px;
  border: 2px solid #64748b;
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
.hero-deal-box h3 { color: var(--accent-amazon); margin-bottom: 8px; font-size: 1.16rem; }

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

.grey-section {
  background-color: var(--bg-section);
  border: 1px solid var(--border-grey);
  border-radius: 12px;
  padding: 26px;
  margin-bottom: 26px;
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
.metric-card .val { font-size: 1.5rem; font-weight: 900; color: #0f172a; }
.metric-card .lbl { font-size: 0.78rem; font-weight: 700; color: #334155; text-transform: uppercase; }
.rec-box {
  background: #ffffff;
  border: 2px solid var(--accent-green);
  border-radius: 8px;
  padding: 16px;
  margin-top: 12px;
}
.rec-box h4 { color: var(--accent-green); font-size: 1.04rem; margin-bottom: 6px; }

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

details.faq-item {
  background: var(--bg-card);
  border: 1px solid var(--border-grey);
  border-radius: 8px;
  padding: 14px 18px;
  margin-bottom: 12px;
}
details.faq-item summary { font-weight: 800; font-size: 1.02rem; cursor: pointer; color: #0f172a; }
details.faq-item p { margin-top: 10px; color: #334155; font-size: 0.95rem; }

.sitemap-columns { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; }
.sitemap-box { background: var(--bg-card); border: 1px solid var(--border-grey); padding: 18px; border-radius: 8px; }
.sitemap-box h3 { margin-bottom: 10px; font-size: 1.1rem; color: #0f172a; }
.sitemap-box ul { padding-left: 18px; font-size: 0.9rem; line-height: 1.8; }

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


def build_article_page(article: dict, recent_articles: list[dict]) -> str:
    related_links = ""
    for rel in recent_articles[:8]:
        if rel["slug"] == article["slug"]:
            continue
        related_links += f"""
        <li>
          <a href="{BASE_URL}/reviews/{rel['slug']}.html"><strong>{rel['title']}</strong></a>
          <span> ({rel['vol_cuft']} Cu. Ft. / {rel['media_type']} — {rel['date']})</span>
        </li>
        """

    bed_scenarios = [
        ("4x4 ft Raised Bed (6-in Depth)", 4.0, 4.0, 6.0),
        ("4x8 ft Raised Bed (9-in Depth)", 4.0, 8.0, 9.0),
        ("6x3 ft Oval Bed (12-in Depth)", 6.0, 3.0, 12.0),
        ("8x4 ft Deep Raised Bed (12-in Depth)", 8.0, 4.0, 12.0),
        ("10x5 ft Garden Plot (3-in Mulch Topdress)", 10.0, 5.0, 3.0),
    ]
    scenario_rows = ""
    for b_name, l_ft, w_ft, d_in in bed_scenarios:
        needed_cuft = round((l_ft * w_ft * (d_in / 12.0)), 1)
        bags_ct = max(1, math.ceil(needed_cuft / max(article["vol_cuft"], 0.5)))
        scenario_rows += f"""
        <tr>
          <td><strong>{b_name}</strong></td>
          <td>{needed_cuft} Cu. Ft. ({round(needed_cuft / 27.0, 2)} Cu. Yd.)</td>
          <td>{bags_ct} x {article['vol_cuft']} Cu. Ft. Units</td>
          <td><a href="{article['affiliate_url']}" target="_blank" rel="nofollow sponsored noopener">Check Amazon Price &rarr;</a></td>
        </tr>
        """

    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": f"How much area does one {article['brand']} {article['model_name']} cover?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": f"Each {article['vol_cuft']} cu. ft. unit of {article['brand']} {article['model_name']} covers approximately {article['cov_3in']} sq. ft. at a 3-inch layer depth."
                }
            },
            {
                "@type": "Question",
                "name": f"How many units are needed for {article['app_title']}?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": f"For {article['target_cuft']} cu. ft. ({article['cu_yards']} cubic yards), you need approximately {article['bags_needed']} units of {article['vol_cuft']} cu. ft. capacity."
                }
            }
        ]
    }

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{article['title']} ({article['date']} Volume &amp; Bag Count Guide)</title>
  <meta name="description" content="Review of {article['brand']} {article['model_name']} ({article['vol_cuft']} cu. ft., {article['media_type']}) for {article['app_title']}. Includes cubic feet &amp; bag calculator." />
  <link rel="canonical" href="{BASE_URL}/reviews/{article['slug']}.html" />
  <meta property="og:title" content="{article['title']}" />
  <meta property="og:description" content="Covers {article['cov_3in']} sq. ft. at 3-in depth per {article['vol_cuft']} cu. ft. unit ({article['media_type']})." />
  <meta property="og:type" content="article" />
  <meta property="og:url" content="{BASE_URL}/reviews/{article['slug']}.html" />
  <style>{GLOBAL_CSS}</style>
  <script type="application/ld+json">{json.dumps(faq_schema)}</script>
</head>
<body>
  <div class="top-promo-banner">
    <span class="badge-live">GARDEN SUPPLY DEAL</span>
    Check Live Amazon Pricing &amp; Multi-Pack Savings on <strong>{article['brand']} {article['model_name']}</strong>
    <a class="banner-cta" href="{article['affiliate_url']}" target="_blank" rel="nofollow sponsored noopener">Check Price on Amazon &rarr;</a>
  </div>

  <header class="site-header">
    <div class="container nav-flex">
      <a href="{BASE_URL}/index.html" class="brand-logo">SoilBag<span>Calc</span></a>
      <ul class="nav-links">
        <li><a href="{BASE_URL}/index.html#calculator">Soil &amp; Mulch Calculator</a></li>
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
        Published: {article['date']} &bull; Category: {article['category']} &bull; Rating: ★ {article['rating']}/5.0
      </div>
      <h1 style="font-size:1.95rem; margin-bottom:14px; color:#0f172a;">{article['title']}</h1>
      <p style="font-size:1.05rem; color:#334155; margin-bottom:20px;">
        Planning a garden project for <strong>{article['app_title']}</strong> is much easier when you convert bed dimensions into exact cubic feet before shopping. Here we evaluate the <strong>{article['brand']} {article['model_name']}</strong> ({article['vol_cuft']} cu. ft. per unit, {article['media_type']}, {article['spec_note']}) and show how it {article['app_benefit']}.
      </p>

      <div class="hero-deal-box" style="margin-bottom:24px; text-align:left; display:flex; flex-wrap:wrap; justify-content:space-between; align-items:center; gap:16px;">
        <div>
          <h3 style="margin-bottom:4px;">{article['brand']} {article['model_name']} — Amazon Availability</h3>
          <p style="color:#cbd5e1; font-size:0.93rem;">{article['brand_tech']} | Unit Volume: {article['vol_cuft']} Cu. Ft. | 3-In Coverage: ~{article['cov_3in']} Sq. Ft.</p>
        </div>
        <a class="btn-amazon" href="{article['affiliate_url']}" target="_blank" rel="nofollow sponsored noopener">Check Current Price on Amazon &rarr;</a>
      </div>

      <h2 class="section-title">1. Material Specifications &amp; Coverage Breakdown</h2>
      <div class="table-wrap" style="margin:16px 0 26px;">
        <table class="comp-table">
          <thead>
            <tr>
              <th>Attribute</th>
              <th>Specification</th>
              <th>Garden Benefit</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Volume Per Unit</strong></td>
              <td>{article['vol_cuft']} Cubic Feet</td>
              <td>Covers ~{article['cov_3in']} sq. ft. at a standard 3-inch layer</td>
            </tr>
            <tr>
              <td><strong>Composition / Material</strong></td>
              <td>{article['media_type']}</td>
              <td>{article['brand_tech']}</td>
            </tr>
            <tr>
              <td><strong>Key Performance Spec</strong></td>
              <td>{article['spec_note']}</td>
              <td>Supports healthy root expansion and consistent moisture</td>
            </tr>
            <tr>
              <td><strong>Target Project Estimate</strong></td>
              <td>{article['target_cuft']} Cu. Ft. ({article['bags_needed']} Units)</td>
              <td>Sized for {article['app_title']}</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2 class="section-title">2. Interactive Bag &amp; Cubic Yard Estimator for {article['brand']}</h2>
      <p class="section-sub">Enter your target volume in cubic feet below to compute how many {article['vol_cuft']} cu. ft. units you need:</p>
      <div class="calc-panel" style="margin-bottom:26px;">
        <div class="calc-grid">
          <div class="form-group">
            <label for="artCuFtInput">Required Volume (Cubic Feet):</label>
            <input type="number" id="artCuFtInput" value="{article['target_cuft']}" min="1" max="500" step="1" oninput="calcArticleBags()" />
          </div>
          <div class="metric-card">
            <div class="lbl">Estimated Units Needed ({article['vol_cuft']} Cu. Ft. Each)</div>
            <div class="val" id="artBagsOut">{article['bags_needed']} Units</div>
            <div style="margin-top:10px;">
              <a class="btn-amazon" href="{article['affiliate_url']}" target="_blank" rel="nofollow sponsored noopener">Shop {article['brand']} on Amazon</a>
            </div>
          </div>
        </div>
      </div>

      <h2 class="section-title">3. Common Garden Bed &amp; Mulch Layer Reference</h2>
      <div class="table-wrap" style="margin:16px 0 26px;">
        <table class="comp-table">
          <thead>
            <tr>
              <th>Bed / Application</th>
              <th>Volume Required</th>
              <th>Estimated Quantity</th>
              <th>Amazon Link</th>
            </tr>
          </thead>
          <tbody>
            {scenario_rows}
          </tbody>
        </table>
      </div>

      <h2 class="section-title">4. Pros, Cons &amp; Buying Verdict</h2>
      <div class="calc-grid" style="margin:16px 0 26px;">
        <div class="calc-panel" style="border-left:5px solid #15803d;">
          <h3 style="color:#15803d; margin-bottom:10px;">Advantages (Pros)</h3>
          <ul style="padding-left:18px; font-size:0.94rem;">
            <li><strong>{article['brand_tech']}</strong> promotes strong root growth and drainage.</li>
            <li>Clear <strong>{article['vol_cuft']} cu. ft.</strong> volume rating simplifies project budgeting.</li>
            <li>Well-suited for <strong>{article['app_title']}</strong>.</li>
          </ul>
        </div>
        <div class="calc-panel" style="border-left:5px solid #b91c1c;">
          <h3 style="color:#b91c1c; margin-bottom:10px;">Considerations (Cons)</h3>
          <ul style="padding-left:18px; font-size:0.94rem;">
            <li>Soil naturally settles 10%–20% after initial watering—factor in a top-off bag if needed.</li>
            <li>Large multi-bed installations may benefit from ordering multi-pack bundles in advance.</li>
          </ul>
        </div>
      </div>

      <div class="hero-deal-box">
        <h3>Ready to Stock Up for {article['app_title']}?</h3>
        <p style="color:#cbd5e1; margin-bottom:14px;">Compare current pack sizes, shipping options, and gardener reviews on Amazon.</p>
        <a class="btn-amazon" href="{article['affiliate_url']}" target="_blank" rel="nofollow sponsored noopener">View {article['brand']} {article['model_name']} on Amazon &rarr;</a>
      </div>
    </article>

    <section class="grey-section">
      <h2 class="section-title">More Daily Soil, Mulch &amp; Raised Bed Reviews</h2>
      <ul style="padding-left:20px; line-height:1.9;">
        {related_links}
      </ul>
    </section>
  </main>

  <footer class="site-footer">
    <div class="container">
      <div class="footer-links">
        <a href="{BASE_URL}/index.html">Home &amp; Soil Calculator</a>
        <a href="{BASE_URL}/index.html#bestsellers">Best Sellers</a>
        <a href="{BASE_URL}/index.html#comparison">Comparison Chart</a>
        <a href="{BASE_URL}/sitemap.html">HTML Site Map</a>
        <a href="{BASE_URL}/sitemap.xml">XML Sitemap</a>
        <a href="{BASE_URL}/feed.xml">RSS Feed</a>
      </div>
      <p>Affiliate Disclosure: SoilBagCalc participates in the Amazon Services LLC Associates Program (StoreID: {AFFILIATE_TAG}). As an Amazon Associate, we earn from qualifying purchases.</p>
    </div>
  </footer>

  <script>
    function calcArticleBags() {{
      var req = parseFloat(document.getElementById('artCuFtInput').value) || 1;
      var perUnit = {article['vol_cuft']};
      var count = Math.max(1, Math.ceil(req / perUnit));
      document.getElementById('artBagsOut').textContent = count + ' Units';
    }}
  </script>
</body>
</html>"""


def build_html_sitemap_page(all_articles: list[dict]) -> str:
    article_links = ""
    for art in all_articles:
        article_links += f"""
        <li>
          <a href="{BASE_URL}/reviews/{art['slug']}.html"><strong>{art['title']}</strong></a>
          <span> — {art['category']} ({art['vol_cuft']} Cu. Ft. | Published {art['date']})</span>
        </li>
        """

    product_links = ""
    for p in CORE_PRODUCTS:
        product_links += f"""
        <li>
          <a href="{amazon_search_url(p['search_query'])}" target="_blank" rel="nofollow sponsored noopener">{p['name']} ({p['bag_cuft']} Cu. Ft.)</a>
          <span> — {p['badge']}</span>
        </li>
        """

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Site Map — SoilBagCalc Garden Soil, Mulch &amp; Raised Bed Calculator</title>
  <meta name="description" content="Complete HTML Site Map indexing all interactive garden soil cubic yard calculators, bag estimators, comparison tables, and {len(all_articles)} daily product reviews." />
  <link rel="canonical" href="{BASE_URL}/sitemap.html" />
  <style>{GLOBAL_CSS}</style>
</head>
<body>
  <header class="site-header">
    <div class="container nav-flex">
      <a href="{BASE_URL}/index.html" class="brand-logo">SoilBag<span>Calc</span></a>
      <ul class="nav-links">
        <li><a href="{BASE_URL}/index.html#calculator">Soil Calculator</a></li>
        <li><a href="{BASE_URL}/index.html#bestsellers">Best Sellers</a></li>
        <li><a href="{BASE_URL}/index.html#comparison">Comparison Table</a></li>
        <li><a href="{BASE_URL}/index.html#daily-reviews">Daily Reviews</a></li>
        <li><a href="{BASE_URL}/sitemap.xml">XML Sitemap</a></li>
      </ul>
    </div>
  </header>

  <main class="container" style="margin-top:24px;">
    <section class="grey-section">
      <h1 class="section-title">SoilBagCalc — Complete HTML Site Map &amp; Archive</h1>
      <p class="section-sub">Index of all interactive garden calculators, comparison tables, XML/RSS feeds, and {len(all_articles)} automated daily product reviews.</p>

      <div class="sitemap-columns" style="margin-bottom:24px;">
        <div class="sitemap-box">
          <h3>Core Calculators &amp; Sections</h3>
          <ul>
            <li><a href="{BASE_URL}/index.html">Homepage &amp; Garden Soil / Mulch Volume Calculator</a></li>
            <li><a href="{BASE_URL}/index.html#calculator">Interactive Cubic Feet, Cubic Yards &amp; Bag Estimator</a></li>
            <li><a href="{BASE_URL}/index.html#search-section">Real-Time Soil, Mulch, Grow Bag &amp; Raised Bed Search</a></li>
            <li><a href="{BASE_URL}/index.html#bestsellers">Top 10 Best-Selling Amazon Garden Products</a></li>
            <li><a href="{BASE_URL}/index.html#comparison">Side-by-Side Technical Comparison Table</a></li>
            <li><a href="{BASE_URL}/index.html#faq">Soil Depth, Cubic Yard &amp; Bag Sizing FAQ</a></li>
          </ul>
        </div>
        <div class="sitemap-box">
          <h3>Search Engine &amp; Syndication Feeds</h3>
          <ul>
            <li><a href="{BASE_URL}/sitemap.xml">XML Sitemap (sitemap.xml)</a></li>
            <li><a href="{BASE_URL}/feed.xml">RSS 2.0 Feed (feed.xml)</a></li>
            <li><a href="{BASE_URL}/robots.txt">Robots Directives (robots.txt)</a></li>
          </ul>
        </div>
      </div>

      <div class="sitemap-box" style="margin-bottom:24px;">
        <h3>All Daily Product Review Articles ({len(all_articles)} Indexed Pages)</h3>
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
      <p>&copy; {datetime.datetime.now(datetime.timezone.utc).year} SoilBagCalc (Amazon StoreID: {AFFILIATE_TAG}). <a href="{BASE_URL}/index.html" style="color:#ffffff;">Return to Calculator</a></p>
    </div>
  </footer>
</body>
</html>"""


def build_index_page(all_articles: list[dict]) -> str:
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
              <li><strong>Unit Volume:</strong> {p['bag_cuft']} Cu. Ft.</li>
              <li><strong>3-In Coverage:</strong> ~{p['coverage_at_3in_sqft']} Sq. Ft.</li>
              <li><strong>Material Mix:</strong> {p['soil_type']}</li>
              <li><strong>Key Spec:</strong> {p['ph_range']}</li>
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
          <td><strong>{p['bag_cuft']} Cu. Ft.</strong></td>
          <td>~{p['coverage_at_3in_sqft']} Sq. Ft.</td>
          <td>{p['soil_type']}</td>
          <td>{p['ph_range']}</td>
          <td>★ {p['rating']}</td>
          <td><a class="btn-amazon" style="padding:7px 12px; font-size:0.82rem;" href="{aff_url}" target="_blank" rel="nofollow sponsored noopener">View Deal</a></td>
        </tr>
        """

    daily_cards = ""
    for art in all_articles[:36]:
        daily_cards += f"""
        <div class="article-card" data-art-search="{art['title'].lower()} {art['brand'].lower()} {art['category'].lower()} {art['app_title'].lower()}">
          <div>
            <div style="font-size:0.78rem; font-weight:700; color:#334155; text-transform:uppercase; margin-bottom:6px;">
              {art['date']} &bull; {art['category']} &bull; {art['vol_cuft']} Cu. Ft.
            </div>
            <h3 style="font-size:1.12rem; margin-bottom:10px;">
              <a href="{BASE_URL}/reviews/{art['slug']}.html" style="color:#0f172a;">{art['title']}</a>
            </h3>
            <p style="font-size:0.9rem; color:#334155; margin-bottom:14px;">
              Requires <strong>{art['bags_needed']} units</strong> ({art['target_cuft']} cu. ft. / {art['cu_yards']} cu. yd.) with {art['brand_tech']}.
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
            "How do I calculate cubic feet and cubic yards of garden soil or mulch?",
            "Multiply your bed Length (ft) by Width (ft) by Depth in inches divided by 12 to get Cubic Feet (Cu. Ft.). Divide Cubic Feet by 27 to get Cubic Yards (Cu. Yd.). For example, an 8 ft x 4 ft bed filled 9 inches deep equals (8 x 4 x 9) / 12 = 24 cubic feet (0.89 cubic yards)."
        ),
        (
            "How many bags of 2 cu. ft. soil or mulch do I need for a project?",
            "Divide your total required cubic feet by the bag size (e.g., 2.0 cu. ft. per bag) and round up to the nearest whole bag. A 16 cu. ft. project requires eight 2 cu. ft. bags."
        ),
        (
            "What depth of mulch should I apply around plants and trees?",
            "Apply a 2- to 3-inch layer of mulch for moisture retention and weed control, keeping mulch a few inches away from tree trunks and plant stems so bark stays dry and healthy."
        ),
        (
            "What depth of soil is best for raised vegetable beds?",
            "Shallow-rooted greens and herbs do well in 6 to 8 inches of soil, while deep-rooted crops like tomatoes, peppers, potatoes, and squash thrive in 12 to 18 inches of loose, well-draining soil."
        ),
        (
            "Should I account for soil settling when ordering bags?",
            "Yes. Loose potting soil, compost, and raised bed mixes settle slightly after initial watering and over the growing season, so having an extra bag or two on hand makes topping off easy."
        ),
        (
            "When does it make sense to use fabric grow bags instead of rigid beds?",
            "Fabric grow bags work well on patios, decks, or small yards where digging is impractical, offering breathable walls that encourage root air-pruning and excess water drainage."
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
            "name": "SoilBagCalc — Garden Soil, Mulch & Raised Bed Volume Calculator",
            "applicationCategory": "UtilitiesApplication",
            "operatingSystem": "All",
            "url": f"{BASE_URL}/index.html",
            "description": "Free interactive garden bed soil, mulch, compost, and bag count calculator with daily product reviews."
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
            "category": p["category"],
            "bag_cuft": p["bag_cuft"],
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
  <title>SoilBagCalc — Garden Soil, Mulch, Compost &amp; Raised Bed Volume Calculator</title>
  <meta name="description" content="Calculate exact cubic feet, cubic yards, and bag counts for garden soil, mulch, compost, and raised beds in seconds. Compare top garden products &amp; daily reviews." />
  <link rel="canonical" href="{BASE_URL}/index.html" />
  <link rel="alternate" type="application/rss+xml" title="SoilBagCalc Daily Garden Reviews RSS" href="{BASE_URL}/feed.xml" />
  <meta property="og:title" content="SoilBagCalc — Interactive Garden Soil, Mulch &amp; Bag Calculator" />
  <meta property="og:description" content="Calculate cubic feet, cubic yards, and bag counts for your raised beds, containers, and mulch borders." />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="{BASE_URL}/index.html" />
  <style>{GLOBAL_CSS}</style>
  <script type="application/ld+json">{json.dumps(json_ld)}</script>
</head>
<body>

  <div class="top-promo-banner">
    <span class="badge-live">GARDEN &amp; PATIO DEALS</span>
    Shop Top-Rated Potting Soil, Raised Garden Beds, Mulch &amp; Fabric Grow Bags on Amazon
    <a class="banner-cta" href="{amazon_search_url('Organic Potting Soil Raised Garden Bed Fabric Grow Bags')}" target="_blank" rel="nofollow sponsored noopener">Browse Today's Amazon Deals &rarr;</a>
  </div>

  <header class="site-header">
    <div class="container nav-flex">
      <a href="{BASE_URL}/index.html" class="brand-logo">SoilBag<span>Calc</span></a>
      <ul class="nav-links">
        <li><a href="#calculator">Soil Calculator</a></li>
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

    <section class="hero-banner">
      <div class="hero-grid">
        <div>
          <h1>Garden Soil, Mulch, Compost &amp; Raised Bed Volume Calculator</h1>
          <p>Enter your bed or garden area dimensions and depth below to calculate exact <strong>Cubic Feet</strong>, <strong>Cubic Yards</strong>, and <strong>Bag Counts</strong>—with instant links to matching garden products on Amazon.</p>
          <div style="display:flex; gap:12px; flex-wrap:wrap;">
            <a class="btn-amazon" href="#calculator">Open Soil Volume Calculator &darr;</a>
            <a class="btn-outline" style="color:#ffffff; border-color:#94a3b8;" href="{amazon_search_url('Best Selling Garden Soil Raised Bed Mulch')}" target="_blank" rel="nofollow sponsored noopener">View Amazon Garden Best Sellers &rarr;</a>
          </div>
        </div>
        <div class="hero-deal-box">
          <h3>🌱 Featured Garden Essentials</h3>
          <p style="color:#e2e8f0; font-size:0.92rem; margin-bottom:14px;">Organic Potting Soil, Galvanized Raised Beds, Hardwood Mulch &amp; Breathable Grow Bags.</p>
          <a class="btn-amazon" style="width:100%;" href="{amazon_search_url('FoxFarm Ocean Forest VEGEGA Raised Garden Bed VIVOSUN Grow Bags')}" target="_blank" rel="nofollow sponsored noopener">Check Live Amazon Prices &rarr;</a>
        </div>
      </div>
    </section>

    <section id="calculator" class="grey-section">
      <h2 class="section-title">Interactive Garden Soil, Mulch &amp; Bag Count Calculator</h2>
      <p class="section-sub">Choose a preset or enter custom dimensions in feet and inches to calculate required volume and bag counts.</p>

      <div class="preset-row">
        <button type="button" class="preset-btn" onclick="setSoilPreset(8, 4, 9, 2.0)">🥕 8&times;4 ft Bed (9-in Soil)</button>
        <button type="button" class="preset-btn" onclick="setSoilPreset(4, 4, 12, 2.0)">🍅 4&times;4 ft Deep Bed (12-in)</button>
        <button type="button" class="preset-btn" onclick="setSoilPreset(20, 4, 3, 2.0)">🌲 20&times;4 ft Mulch Strip (3-in)</button>
        <button type="button" class="preset-btn" onclick="setSoilPreset(6, 3, 12, 1.5)">🌿 6&times;3 ft Oval Bed (12-in)</button>
        <button type="button" class="preset-btn" onclick="setSoilPreset(12, 10, 2, 1.0)">🌾 12&times;10 ft Compost Topdress (2-in)</button>
      </div>

      <div class="calc-grid">
        <div class="calc-panel">
          <div class="form-row">
            <div class="form-group">
              <label for="slLength">1. Length (Feet):</label>
              <input type="number" id="slLength" value="8" min="1" max="200" step="0.5" oninput="calculateSoil()" />
            </div>
            <div class="form-group">
              <label for="slWidth">2. Width (Feet):</label>
              <input type="number" id="slWidth" value="4" min="1" max="200" step="0.5" oninput="calculateSoil()" />
            </div>
          </div>
          <div class="form-row">
            <div class="form-group">
              <label for="slDepth">3. Depth (Inches):</label>
              <input type="number" id="slDepth" value="9" min="0.5" max="48" step="0.5" oninput="calculateSoil()" />
            </div>
            <div class="form-group">
              <label for="slBagSize">4. Bag / Unit Size (Cubic Feet):</label>
              <select id="slBagSize" onchange="calculateSoil()">
                <option value="1.0">1.0 Cu. Ft. Bag</option>
                <option value="1.5">1.5 Cu. Ft. Bag</option>
                <option value="2.0" selected>2.0 Cu. Ft. Standard Bag</option>
                <option value="3.0">3.0 Cu. Ft. Large Bag</option>
              </select>
            </div>
          </div>
        </div>

        <div class="calc-panel">
          <h3 style="margin-bottom:12px; color:#0f172a;">Calculated Material Requirements</h3>
          <div class="metrics-grid">
            <div class="metric-card">
              <div class="val" id="outCuFt">24.0 Cu. Ft.</div>
              <div class="lbl">Total Volume (Cu. Ft.)</div>
            </div>
            <div class="metric-card">
              <div class="val" id="outCuYd">0.89 Cu. Yd.</div>
              <div class="lbl">Cubic Yards</div>
            </div>
            <div class="metric-card">
              <div class="val" id="outBags">12 Bags</div>
              <div class="lbl">Estimated Bags Needed</div>
            </div>
            <div class="metric-card">
              <div class="val" id="outArea">32.0 Sq. Ft.</div>
              <div class="lbl">Surface Area</div>
            </div>
          </div>

          <div id="dynamicSoilRec" class="rec-box"></div>
        </div>
      </div>
    </section>

    <section id="search-section" class="grey-section">
      <h2 class="section-title">Search Garden Soil, Mulch, Grow Bags &amp; Raised Beds</h2>
      <p class="section-sub">Filter products and daily reviews by keyword or category, or search directly on Amazon.</p>
      <div class="search-bar">
        <input type="text" id="soilSearchInput" class="search-input" placeholder="Search FoxFarm, Miracle-Gro, VIVOSUN, VEGEGA, mulch, compost, grow bags..." oninput="filterSoilCatalog()" />
        <select id="soilCatSelect" class="filter-select" onchange="filterSoilCatalog()">
          <option value="ALL">All Categories</option>
          <option value="Potting & Raised Bed Soil">Potting &amp; Raised Bed Soil</option>
          <option value="Garden Mulch & Compost">Garden Mulch &amp; Compost</option>
          <option value="Fabric Grow Bags">Fabric Grow Bags</option>
          <option value="Metal Raised Garden Beds">Metal Raised Garden Beds</option>
        </select>
        <button type="button" class="btn-amazon" onclick="searchSoilAmazonDirect()">Search Live on Amazon &rarr;</button>
      </div>
      <p id="soilFilterStatus" style="font-size:0.88rem; font-weight:700; color:#334155;">Showing all 10 top-rated garden products below:</p>
    </section>

    <section id="bestsellers" class="grey-section">
      <h2 class="section-title">Best-Selling Soil, Mulch, Grow Bags &amp; Raised Garden Beds</h2>
      <p class="section-sub">Popular options for raised beds, containers, and yard landscaping on Amazon.</p>
      <div id="soilBestSellersGrid" class="product-grid">
        {bestsellers_cards}
      </div>
    </section>

    <section id="comparison" class="grey-section">
      <h2 class="section-title">Side-by-Side Garden Product Comparison</h2>
      <p class="section-sub">Compare volume per unit, 3-inch coverage area, composition, and key specs.</p>
      <div class="table-wrap">
        <table class="comp-table">
          <thead>
            <tr>
              <th>Product</th>
              <th>Category</th>
              <th>Unit Volume</th>
              <th>3-In Coverage</th>
              <th>Material Mix</th>
              <th>Key Spec</th>
              <th>Rating</th>
              <th>Amazon Link</th>
            </tr>
          </thead>
          <tbody>
            {comparison_rows}
          </tbody>
        </table>
      </div>
    </section>

    <section id="daily-reviews" class="grey-section">
      <h2 class="section-title">Daily Automated Product Reviews &amp; Sizing Guides</h2>
      <p class="section-sub">Updated automatically with <strong>3 new product review articles every day</strong>. Currently live: <strong>{len(all_articles)}</strong> articles:</p>
      <div id="dailySoilReviewsGrid" class="articles-grid">
        {daily_cards}
      </div>
    </section>

    <section id="faq" class="grey-section">
      <h2 class="section-title">Frequently Asked Questions (Soil, Mulch &amp; Raised Bed Sizing)</h2>
      <p class="section-sub">Quick reference answers for measuring beds, estimating bags, and planning seasonal planting.</p>
      {faq_html}
    </section>

    <section id="sitemap-section" class="grey-section">
      <h2 class="section-title">Site Map &amp; Content Directory</h2>
      <p class="section-sub">Links to calculators, comparison tables, XML/RSS feeds, and daily review pages.</p>
      <div class="sitemap-columns">
        <div class="sitemap-box">
          <h3>Main Pages &amp; Feeds</h3>
          <ul>
            <li><a href="#calculator">Garden Soil, Mulch &amp; Bag Calculator</a></li>
            <li><a href="#bestsellers">Best-Selling Garden Products</a></li>
            <li><a href="#comparison">Side-by-Side Comparison Table</a></li>
            <li><a href="{BASE_URL}/sitemap.html"><strong>Full HTML Site Map ({len(all_articles)} Reviews)</strong></a></li>
            <li><a href="{BASE_URL}/sitemap.xml">XML Sitemap (sitemap.xml)</a></li>
            <li><a href="{BASE_URL}/feed.xml">RSS 2.0 Feed (feed.xml)</a></li>
          </ul>
        </div>
        <div class="sitemap-box">
          <h3>Recent Daily Review Articles</h3>
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
        <a href="#calculator">Soil Calculator</a>
        <a href="#search-section">Product Search</a>
        <a href="#bestsellers">Best Sellers</a>
        <a href="#comparison">Comparison Table</a>
        <a href="#daily-reviews">Daily Reviews</a>
        <a href="#faq">FAQ</a>
        <a href="{BASE_URL}/sitemap.html">HTML Site Map</a>
        <a href="{BASE_URL}/sitemap.xml">XML Sitemap</a>
        <a href="{BASE_URL}/feed.xml">RSS Feed</a>
      </div>
      <p style="margin-bottom:8px;"><strong>Amazon Affiliate Disclosure:</strong> SoilBagCalc participates in the Amazon Services LLC Associates Program (Affiliate StoreID: <code>{AFFILIATE_TAG}</code>), an affiliate advertising program designed to provide a means for sites to earn advertising fees by linking to Amazon.com.</p>
      <p>&copy; {datetime.datetime.now(datetime.timezone.utc).year} SoilBagCalc. Automated via GitHub Actions.</p>
    </div>
  </footer>

  <script>
    var SOIL_PRODUCTS = {js_products};
    var AFFILIATE_TAG = "{AFFILIATE_TAG}";

    function setSoilPreset(len, wid, depthIn, bagCuFt) {{
      document.getElementById('slLength').value = len;
      document.getElementById('slWidth').value = wid;
      document.getElementById('slDepth').value = depthIn;
      document.getElementById('slBagSize').value = bagCuFt.toString();
      calculateSoil();
    }}

    function calculateSoil() {{
      var len = parseFloat(document.getElementById('slLength').value) || 4;
      var wid = parseFloat(document.getElementById('slWidth').value) || 4;
      var depthIn = parseFloat(document.getElementById('slDepth').value) || 6;
      var bagSize = parseFloat(document.getElementById('slBagSize').value) || 2.0;

      var area = +(len * wid).toFixed(1);
      var cuFt = +((len * wid * (depthIn / 12.0))).toFixed(1);
      var cuYd = +(cuFt / 27.0).toFixed(2);
      var bags = Math.max(1, Math.ceil(cuFt / bagSize));

      document.getElementById('outCuFt').textContent = cuFt.toLocaleString() + ' Cu. Ft.';
      document.getElementById('outCuYd').textContent = cuYd + ' Cu. Yd.';
      document.getElementById('outBags').textContent = bags.toLocaleString() + ' Bags';
      document.getElementById('outArea').textContent = area.toLocaleString() + ' Sq. Ft.';

      var match = SOIL_PRODUCTS.find(function(p) {{ return p.bag_cuft >= bagSize; }}) || SOIL_PRODUCTS[0];
      var shopAllUrl = 'https://www.amazon.com/s?k=' + encodeURIComponent(bagSize + ' cu ft garden soil raised bed mix') + '&tag=' + AFFILIATE_TAG;
      var mulchUrl = 'https://www.amazon.com/s?k=' + encodeURIComponent('garden mulch ' + bagSize + ' cu ft') + '&tag=' + AFFILIATE_TAG;

      document.getElementById('dynamicSoilRec').innerHTML =
        '<h4>✅ Estimated Order: ' + bags + ' x ' + bagSize + ' Cu. Ft. (' + cuFt + ' Cu. Ft. Total)</h4>' +
        '<p style="font-size:0.9rem; color:#334155; margin-bottom:10px;"><strong>Featured Match:</strong> ' + match.name + ' — ' + match.highlight + '</p>' +
        '<div style="display:flex; gap:8px; flex-wrap:wrap;">' +
        '<a class="btn-amazon" href="' + match.url + '" target="_blank" rel="nofollow sponsored noopener">Check ' + match.brand + ' on Amazon &rarr;</a>' +
        '<a class="btn-outline" href="' + shopAllUrl + '" target="_blank" rel="nofollow sponsored noopener">Shop ' + bagSize + ' Cu. Ft. Soil</a>' +
        '<a class="btn-outline" href="' + mulchUrl + '" target="_blank" rel="nofollow sponsored noopener">Shop Mulch &amp; Compost</a>' +
        '</div>';
    }}

    function filterSoilCatalog() {{
      var q = (document.getElementById('soilSearchInput').value || '').toLowerCase().trim();
      var cat = document.getElementById('soilCatSelect').value;
      var cards = document.querySelectorAll('#soilBestSellersGrid .product-card');
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

      var artCards = document.querySelectorAll('#dailySoilReviewsGrid .article-card');
      artCards.forEach(function(ac) {{
        var aSearch = ac.getAttribute('data-art-search') || '';
        ac.style.display = (!q || aSearch.indexOf(q) !== -1) ? 'flex' : 'none';
      }});

      document.getElementById('soilFilterStatus').textContent =
        'Showing ' + shown + ' matching product(s) (and filtered daily review articles below):';
    }}

    function searchSoilAmazonDirect() {{
      var q = document.getElementById('soilSearchInput').value.trim() || 'Garden Soil Raised Bed Mulch Grow Bags';
      window.open('https://www.amazon.com/s?k=' + encodeURIComponent(q) + '&tag=' + AFFILIATE_TAG, '_blank');
    }}

    calculateSoil();
  </script>
</body>
</html>"""


def generate_sitemaps_and_feeds(all_articles: list[dict]) -> list[str]:
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

    html_sitemap = build_html_sitemap_page(all_articles)
    with open(os.path.join(OUTPUT_DIR, "sitemap.html"), "w", encoding="utf-8") as f:
        f.write(html_sitemap)

    robots_txt = f"""User-agent: *
Allow: /

Sitemap: {BASE_URL}/sitemap.xml
"""
    with open(os.path.join(OUTPUT_DIR, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(robots_txt)

    rss_items = ""
    for art in all_articles[:30]:
        u = f"{BASE_URL}/reviews/{art['slug']}.html"
        rss_items += f"""    <item>
      <title><![CDATA[{art['title']}]]></title>
      <link>{u}</link>
      <guid>{u}</guid>
      <pubDate>{art['date']}T04:30:00Z</pubDate>
      <description><![CDATA[Volume and bag estimator review for {art['brand']} {art['model_name']} ({art['vol_cuft']} cu. ft.) on {art['app_title']}.]]></description>
    </item>\n"""

    rss_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>SoilBagCalc — Daily Garden Soil, Mulch &amp; Raised Bed Reviews</title>
    <link>{BASE_URL}/index.html</link>
    <description>Automated daily product reviews and volume calculators for garden soil, mulch, compost, and raised beds.</description>
    <language>en-us</language>
{rss_items}  </channel>
</rss>"""

    with open(os.path.join(OUTPUT_DIR, "feed.xml"), "w", encoding="utf-8") as f:
        f.write(rss_xml)

    with open(os.path.join(OUTPUT_DIR, f"{INDEXNOW_KEY}.txt"), "w", encoding="utf-8") as f:
        f.write(INDEXNOW_KEY)

    return urls


def ping_indexnow(newly_added: list[dict]):
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
            print(f"[IndexNow] Pinged {len(url_list)} URLs (HTTP {resp.status})")
    except Exception as exc:
        print(f"[IndexNow] Notice: {exc}")


def main():
    os.makedirs(REVIEWS_DIR, exist_ok=True)
    all_articles, newly_added = load_and_advance_state()

    index_html = build_index_page(all_articles)
    with open(os.path.join(OUTPUT_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_html)

    for art in all_articles:
        page_html = build_article_page(art, all_articles)
        out_path = os.path.join(REVIEWS_DIR, f"{art['slug']}.html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(page_html)

    generate_sitemaps_and_feeds(all_articles)
    ping_indexnow(newly_added)
    print(f"SoilBagCalc built! Total articles: {len(all_articles)} (+{len(newly_added)} new).")


if __name__ == "__main__":
    main()
