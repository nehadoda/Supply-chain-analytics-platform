import duckdb
import pandas as pd
import os

# ── Configuration ──────────────────────────────────────────────────────────────

DB_PATH = r"C:\Users\itsme\OneDrive - VisaVoyageConsultant\Desktop\Neha\Sales-analytics-platform\Sales_analytics\Analytics.duckdb"

OUTPUT_FOLDER = "data_processed"

TABLES = [
    # Fact tables (for analysis in Power BI)
    "fct_sales_with_currency",
    "fct_profit_analysis",
    "fct_price_comparision",
    "fct_currency_impact",
    # Dimension tables (for filters and relationships in Power BI)
    "dim_product",
    "dim_country",
    "dim_currency",
]

# ── Setup ───────────────────────────────────────────────────────────────────────

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# ── Connect to DuckDB ───────────────────────────────────────────────────────────

print("🔌 Connecting to DuckDB...")
try:
    con = duckdb.connect(DB_PATH, read_only=True)
    print("✅ Connected successfully!\n")
except Exception as e:
    print(f"❌ Could not connect to DuckDB: {e}")
    print("👉 Make sure VS Code terminal is closed and dbt is not running.")
    exit(1)

# ── Export Each Table ───────────────────────────────────────────────────────────

print("📤 Exporting tables to data_processed/...\n")

success_count = 0
fail_count = 0

for table in TABLES:
    try:
        df = con.execute(f"SELECT * FROM {table}").df()
        output_path = os.path.join(OUTPUT_FOLDER, f"{table}.csv")
        df.to_csv(output_path, index=False)
        print(f"  ✅ {table:<35} → {len(df):>6} rows → {output_path}")
        success_count += 1
    except Exception as e:
        print(f"  ❌ {table:<35} → FAILED: {e}")
        fail_count += 1

# ── Close Connection ────────────────────────────────────────────────────────────

con.close()

# ── Summary ─────────────────────────────────────────────────────────────────────

print(f"\n{'─' * 55}")
print(f"  ✅ Successfully exported : {success_count} tables")
if fail_count > 0:
    print(f"  ❌ Failed               : {fail_count} tables")
print(f"{'─' * 55}")
print(f"\n🎉 Done! Go to Power BI and press Alt+F5 to refresh.\n")