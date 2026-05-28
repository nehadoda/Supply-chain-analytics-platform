import subprocess
import os

print("🚀 Starting full pipeline refresh...\n")

# Step 1 — Ingest fresh data
print("📥 Step 1: Ingesting raw data...")
subprocess.run(["python", "scripts/ingest_data.py"], check=True)

# Step 2 — Prepare seeds
print("🌱 Step 2: Preparing dbt seeds...")
subprocess.run(["python", "scripts/prepare_seeds.py"], check=True)

# Step 3 — Run dbt
print("⚙️  Step 3: Running dbt pipeline...")
os.chdir("sales_analytics")
subprocess.run(["dbt", "seed"], check=True)
subprocess.run(["dbt", "run"], check=True)
subprocess.run(["dbt", "test"], check=True)
os.chdir("..")

# Step 4 — Export to Power BI
print("📊 Step 4: Exporting to Power BI...")
subprocess.run(["python", "scripts/export_to_powerbi.py"], check=True)

print("\n✅ Pipeline complete! Go refresh Power BI now.")