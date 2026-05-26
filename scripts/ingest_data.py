import os
import requests
import pandas as pd
from bs4 import BeautifulSoup

# Smart directory check: If we are already running inside 'data_raw', 
# we drop files here. Otherwise, we look for or create a 'data_raw' folder.
current_folder = os.path.basename(os.getcwd())
if current_folder == "data_raw":
    RAW_DATA_DIR = "" # Save directly in the current directory
    print("📍 Script running INSIDE 'data_raw'. Files will land here directly.")
else:
    RAW_DATA_DIR = "data_raw" # Save inside a subfolder named 'data_raw'
    os.makedirs(RAW_DATA_DIR, exist_ok=True)
    print("📍 Script running outside. Files will land in 'data_raw/' subfolder.")

print("🚀 Starting Phase 1: Data Ingestion...")


# ==========================================
# SOURCE 1: EXCEL DATA (E-Commerce Sample)
# ==========================================
def ingest_excel_source():
    print("\n📥 Source 1: Fetching Excel dataset...")
    excel_url = "https://go.microsoft.com/fwlink/?LinkID=521962" 
    output_path = os.path.join(RAW_DATA_DIR, "raw_sales_data.xlsx") if RAW_DATA_DIR else "raw_sales_data.xlsx"
    
    response = requests.get(excel_url)
    if response.status_code == 200:
        with open(output_path, "wb") as f:
            f.write(response.content)
        print(f"✅ Excel data successfully saved to: {output_path if RAW_DATA_DIR else 'Current Folder'}")
    else:
        print(f"❌ Failed to download Excel file. Status code: {response.status_code}")


# ==========================================
# SOURCE 2: API DATA (Semi-Structured JSON)
# ==========================================
def ingest_api_source():
    print("\n📥 Source 2: Fetching live Currency Exchange API data...")
    api_url = "https://open.er-api.com/v6/latest/USD"
    output_path = os.path.join(RAW_DATA_DIR, "currency_rates.json") if RAW_DATA_DIR else "currency_rates.json"
    
    response = requests.get(api_url)
    if response.status_code == 200:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(response.text)
        print(f"✅ API JSON data successfully saved to: {output_path if RAW_DATA_DIR else 'Current Folder'}")
    else:
        print(f"❌ Failed to query API. Status code: {response.status_code}")


# ==========================================
# SOURCE 3: WEB SCRAPING (Unstructured Data)
# ==========================================
def ingest_web_scraped_source():
    print("\n📥 Source 3: Scraping live data from website...")
    scrape_url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
    output_path = os.path.join(RAW_DATA_DIR, "scraped_competitor_prices.csv") if RAW_DATA_DIR else "scraped_competitor_prices.csv"
    
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    response = requests.get(scrape_url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        
        products = []
        for item in soup.find_all("div", class_="thumbnail"):
            title = item.find("a", class_="title").text.strip()
            price = item.find("h4", class_="price").text.strip()
            description = item.find("p", class_="description").text.strip()
            
            products.append({
                "product_name": title,
                "competitor_price": price,
                "description_snippet": description
            })
        
        df = pd.DataFrame(products)
        df.to_csv(output_path, index=False)
        print(f"✅ Web scraped data successfully saved to: {output_path if RAW_DATA_DIR else 'Current Folder'}")
    else:
        print(f"❌ Web scraping blocked or failed. Status code: {response.status_code}")


# ==========================================
# PIPELINE RUNNER CONTROL
# ==========================================
if __name__ == "__main__":
    ingest_excel_source()
    ingest_api_source()
    ingest_web_scraped_source()
    print("\n🎉 Phase 1 Complete! All 3 unique file types have successfully landed.")
