import pandas as pd
import json
import shutil
import os

# ── Dynamic Paths (works on Windows and GitHub Actions Linux) ──────────────────

# This finds the project root regardless of where the script is run from
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

data_raw = os.path.join(BASE_DIR, "data_raw")
seeds    = os.path.join(BASE_DIR, "sales_analytics", "seeds")

print(f"📁 Project root : {BASE_DIR}")
print(f"📁 Data raw     : {data_raw}")
print(f"📁 Seeds folder : {seeds}\n")

os.makedirs(seeds, exist_ok=True)

# ── 1. Convert Excel to CSV ────────────────────────────────────────────────────

print("Converting sales Excel to CSV...")
df_sales = pd.read_excel(os.path.join(data_raw, "raw_sales_data.xlsx"))
df_sales.to_csv(os.path.join(seeds, "raw_sales.csv"), index=False)
print(f"✅ Sales rows: {len(df_sales)}")

# ── 2. Flatten Currency JSON to CSV ───────────────────────────────────────────

print("Converting currency JSON to CSV...")
with open(os.path.join(data_raw, "currency_rates.json")) as f:
    data = json.load(f)

rates = [
    {
        "base_code"      : data["base_code"],
        "target_currency": k,
        "exchange_rate"  : v,
        "last_updated"   : data["time_last_update_utc"]
    }
    for k, v in data["rates"].items()
]

df_currency = pd.DataFrame(rates)
df_currency.to_csv(os.path.join(seeds, "raw_currency_rates.csv"), index=False)
print(f"✅ Currency rows: {len(df_currency)}")

# ── 3. Copy Competitor CSV directly ───────────────────────────────────────────

print("Copying competitor prices CSV...")
shutil.copy(
    os.path.join(data_raw, "scraped_competitor_prices.csv"),
    os.path.join(seeds,    "raw_competitor_prices.csv")
)
print("✅ Competitor prices copied!")

print("\n🎉 All files ready in seeds folder!")