import duckdb
import pandas as pd
import os

# ── Dynamic Paths (works on Windows and GitHub Actions Linux) ──────────────────

# This finds the project root regardless of where the script is run from
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Finds the dbt folder automatically — checks both casings to be safe
def find_dbt_folder():
    for name in ["sales_analytics", "Sales_analytics", "Sales_Analytics"]:
        path = os.path.join(BASE_DIR, name)
        if os.path.exists(path):
            return path
    raise FileNotFoundError("Could not find dbt project folder. Expected 'sales_analytics'.")

DBT_FOLDER    = find_dbt_folder()
DB_PATH       = os.path.join(DBT_FOLDER, "Analytics.duckdb")
OUTPUT_FOLDER = os.path.join(BASE_DIR, "data_processed")

print(f"📁 Project root  : {BASE_DIR}")
print(f"📁 DuckDB path   : {DB_PATH}")
print(f"📁 Output folder : {OUTPUT_FOLDER}\n")

# ── Tables to Export ───────────────────────────────────────────────────────────

TABLES = [
    # Fact tables
    "fct_sales_with_currency",
    "fct_profit_analysis",
    "fct_price_comparision",   # note: keeping your original spelling
    "fct_currency_impact",
    # Dimension tables
    "dim_product",
    "dim_country",
    "dim_currency",
]

# ── Setup ──────────────────────────────────────────────────────────────────────

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# ── Connect to DuckDB ──────────────────────────────────────────────────────────

print("🔌 Connecting to DuckDB...")
try:
    con = duckdb.connect(DB_PATH, read_only=True)
    print("✅ Connected successfully!\n")
except Exception as e:
    print(f"❌ Could not connect to DuckDB: {e}")
    print("👉 Make sure VS Code terminal is closed and dbt is not running.")
    exit(1)

# ── Export Each Table ──────────────────────────────────────────────────────────

print("📤 Exporting tables to data_processed/...\n")

success_count = 0
fail_count    = 0

for table in TABLES:
    try:
        df          = con.execute(f"SELECT * FROM {table}").df()
        output_path = os.path.join(OUTPUT_FOLDER, f"{table}.csv")
        df.to_csv(output_path, index=False)
        print(f"  ✅ {table:<35} → {len(df):>6} rows → {output_path}")
        success_count += 1
    except Exception as e:
        print(f"  ❌ {table:<35} → FAILED: {e}")
        fail_count += 1

# ── Close Connection ───────────────────────────────────────────────────────────

con.close()

# ── Summary ────────────────────────────────────────────────────────────────────

print(f"\n{'─' * 55}")
print(f"  ✅ Successfully exported : {success_count} tables")
if fail_count > 0:
    print(f"  ❌ Failed               : {fail_count} tables")
print(f"{'─' * 55}")
print(f"\n🎉 Done! Go to Power BI and press Alt+F5 to refresh.\n")