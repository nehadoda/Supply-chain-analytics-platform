# Retail Pricing & Market Intelligence Analytics Platform

> An end-to-end analytics engineering project built with Python, dbt, DuckDB, and Power BI.

---

## Project Overview

This platform simulates a modern analytics engineering workflow for a retail business. It integrates data from three real-world sources — structured sales data, live currency exchange rates, and scraped competitor pricing — to deliver a unified pricing intelligence and business performance analytics solution.

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        DATA SOURCES                         │
│  Excel (.xlsx)       REST API (JSON)     Web Scraping (HTML) │
│  Microsoft Sales     Currency Rates      Competitor Prices   │
└──────────┬───────────────────┬───────────────────┬──────────┘
           │                   │                   │
           ▼                   ▼                   ▼
┌─────────────────────────────────────────────────────────────┐
│                   INGESTION — Python                        │
│   pandas           requests              BeautifulSoup      │
│   read_excel()     API fetch             HTML → CSV         │
└──────────────────────────────┬──────────────────────────────┘
                               │  CSV seeds
                               ▼
┌─────────────────────────────────────────────────────────────┐
│              TRANSFORMATION & MODELLING — dbt + DuckDB      │
│                                                             │
│  Staging Layer                                              │
│  ├── stg_sales           (clean, typed, date parsed)        │
│  ├── stg_currency_rates  (flattened JSON, validated)        │
│  └── stg_competitor_prices ($ stripped, nulls removed)      │
│                                                             │
│  Mart Layer                                                 │
│  ├── fct_sales_with_currency   (multi-currency revenue)     │
│  ├── fct_profit_analysis       (margin % by product)        │
│  ├── fct_price_comparison      (us vs competitor)           │
│  └── fct_currency_impact       (revenue in local currency)  │
│                                                             │
│  dbt tests: not_null, unique, relationship checks           │
└──────────────────────────────┬──────────────────────────────┘
                               │  Live ODBC (read-only)
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                   VISUALISATION — Power BI                  │
│  Sales Overview · Profit Analysis                           │
│  Pricing Intelligence · Currency Impact                     │
└─────────────────────────────────────────────────────────────┘
```

---

## Business Problem

Retail businesses operate in competitive, dynamic markets where pricing decisions are shaped by competitor behaviour, currency fluctuations, and internal product performance. This project answers:

- Which products have the highest and lowest profit margins?
- How do our prices compare to competitors?
- What is the real revenue impact of currency fluctuations across countries?
- Which segments and countries drive the most value?

---

## Data Sources

| Source | Format | Description |
|--------|--------|-------------|
| Microsoft sample sales dataset | `.xlsx` | Internal sales transactions across segments, countries, and products |
| ExchangeRate-API | `.json` | Live USD-based exchange rates for 150+ currencies |
| Competitor e-commerce site | HTML → `.csv` | Scraped product names, prices, and descriptions |

---

## Tech Stack

| Layer | Tools |
|-------|-------|
| Ingestion | Python, pandas, requests, BeautifulSoup |
| Storage | DuckDB (local analytical database) |
| Transformation | dbt (dbt-duckdb adapter) |
| Visualisation | Power BI Desktop (live ODBC connection) |
| Version Control | Git & GitHub |
| Environment | VS Code, Jupyter Notebooks |

---

## Project Structure

```
Sales-analytics-platform/
├── data_raw/                        # Raw ingested files
│   ├── raw_sales_data.xlsx
│   ├── currency_rates.json
│   └── scraped_competitor_prices.csv
│
├── data_processed/                  # Exported mart tables (CSV)
│
├── scripts/
│   ├── ingest_data.py               # Multi-source ingestion pipeline
│   ├── prepare_seeds.py             # Converts raw files to dbt seeds
│   └── export_to_powerbi.py         # Exports marts to CSV
│
├── sales_analytics/                 # dbt project
│   ├── seeds/
│   │   ├── raw_sales.csv
│   │   ├── raw_currency_rates.csv
│   │   └── raw_competitor_prices.csv
│   ├── models/
│   │   ├── staging/
│   │   │   ├── stg_sales.sql
│   │   │   ├── stg_currency_rates.sql
│   │   │   ├── stg_competitor_prices.sql
│   │   │   └── schema.yml
│   │   └── marts/
│   │       ├── fct_sales_with_currency.sql
│   │       ├── fct_profit_analysis.sql
│   │       ├── fct_price_comparison.sql
│   │       ├── fct_currency_impact.sql
│   │       └── schema.yml
│   └── dbt_project.yml
│
├── notebooks/                       # Exploratory analysis
├── powerbi/                         # Power BI dashboard file
├── docs/                            # Architecture docs
└── README.md
```

---

## dbt Data Models

### Staging Layer
Cleans and standardises each raw source individually. No business logic — just data quality.

| Model | Key Transformations |
|-------|-------------------|
| `stg_sales` | Type casting, date parsing with MAKE_DATE(), column renaming |
| `stg_currency_rates` | Flattened JSON rates, nulls removed, validated exchange rates |
| `stg_competitor_prices` | Dollar sign stripped, price cast to DOUBLE, trimmed strings |

### Mart Layer
Business-ready tables that combine sources and add analytical logic.

| Model | Description | Key Metric |
|-------|-------------|-----------|
| `fct_sales_with_currency` | Sales joined with exchange rates | Revenue in multiple currencies |
| `fct_profit_analysis` | Aggregated profit by product/country/segment | Profit margin % |
| `fct_price_comparison` | Our prices vs competitor prices | Price position (cheaper/expensive) |
| `fct_currency_impact` | Country revenue in local currency | Currency impact in USD |

---

## Key Business Insights

- **Profit margin analysis** by product and country reveals which lines to prioritise and which to review
- **Price positioning** shows how internal pricing compares to market — product by product
- **Currency impact modelling** quantifies the real revenue effect of exchange rate movements across five countries
- **Segment performance** tracks Government, Midmarket, Enterprise, Small Business, and Channel Partners

---

## How to Run

### 1. Clone the repository
```bash
git clone https://github.com/nehadoda/Sales-analytics-platform.git
cd Sales-analytics-platform
```

### 2. Install dependencies
```bash
pip install pandas requests beautifulsoup4 openpyxl dbt-duckdb
```

### 3. Run ingestion
```bash
python scripts/ingest_data.py
```

### 4. Prepare dbt seeds
```bash
python scripts/prepare_seeds.py
```

### 5. Run dbt pipeline
```bash
cd sales_analytics
dbt seed        # Load raw CSVs into DuckDB
dbt run         # Build staging and mart models
dbt test        # Run data quality checks
dbt docs serve  # View auto-generated documentation
```

### 6. Connect Power BI
Open Power BI → Get Data → ODBC → Use connection string:
```
Driver={DuckDB Driver};Database=<path-to>/sales_analytics/Analytics.duckdb;access_mode=read_only
```

---

## Current Progress

- [x] Project structure and GitHub setup
- [x] Multi-source ingestion pipeline (Excel, API, Web Scraping)
- [x] dbt staging models with data quality tests
- [x] dbt mart models (4 analytical fact tables)
- [x] Power BI live connection via ODBC
- [ ] Power BI dashboard pages
- [ ] Automated pipeline scheduling

---

## Future Enhancements

- GitHub Actions for automated pipeline scheduling
- Incremental dbt models for large datasets
- Forecasting models for pricing and sales trends
- Cloud deployment (BigQuery or Snowflake)
- Real-time API ingestion with streaming

---

## Author

**Neha Doda**  
Data Analyst | Power BI Developer | Analytics Engineer  
[GitHub](https://github.com/nehadoda) 