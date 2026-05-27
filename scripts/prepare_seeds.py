import pandas as pd
import json
import shutil
import os

# ---- Paths ----
data_raw = "data_raw"
seeds = "sales_analytics/seeds"

# ---- 1. Convert Excel to CSV ----
print("Converting sales Excel to CSV...")
df_sales = pd.read_excel(f"{data_raw}/raw_sales_data.xlsx")
df_sales.to_csv(f"{seeds}/raw_sales.csv", index=False)
print(f"✅ Sales rows: {len(df_sales)}")

# ---- 2. Flatten Currency JSON to CSV ----
print("Converting currency JSON to CSV...")
with open(f"{data_raw}/currency_rates.json") as f:
    data = json.load(f)

rates = [
    {
        "base_code": data["base_code"],
        "target_currency": k,
        "exchange_rate": v,
        "last_updated": data["time_last_update_utc"]
    }
    for k, v in data["rates"].items()
]
df_currency = pd.DataFrame(rates)
df_currency.to_csv(f"{seeds}/raw_currency_rates.csv", index=False)
print(f"✅ Currency rows: {len(df_currency)}")

# ---- 3. Copy Competitor CSV directly ----
print("Copying competitor prices CSV...")
shutil.copy(
    f"{data_raw}/scraped_competitor_prices.csv",
    f"{seeds}/raw_competitor_prices.csv"
)
print("✅ Competitor prices copied!")

print("\n🎉 All files ready in seeds folder!")