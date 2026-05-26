# Retail Pricing & Market Intelligence Analytics Platform

## Project Overview

This project is an end-to-end analytics engineering and business intelligence solution designed to integrate and analyze data from multiple real-world sources.

The platform combines:
- Structured sales data from Microsoft sample datasets
- Semi-structured currency exchange data from a live API
- Unstructured competitor pricing data collected through web scraping

The objective of this project is to simulate a modern analytics workflow involving data ingestion, transformation, integration, and visualization to support pricing intelligence and business decision-making.

---

## Business Problem

Retail businesses operate in highly competitive and dynamic markets where pricing strategies are influenced by:
- Competitor pricing
- Currency fluctuations
- Product performance trends

This project aims to:
- Analyze internal sales performance
- Monitor competitor product pricing
- Understand external currency impacts
- Build a unified analytics platform for business insights

---

## Data Sources

### 1. Structured Data (Excel)
Source:
- Microsoft sample sales dataset

Format:
- `.xlsx`

Purpose:
- Internal sales and transactional analysis

---

### 2. Semi-Structured Data (API)
Source:
- Currency Exchange Rate API

Format:
- `.json`

Purpose:
- Analyze external currency fluctuation impact on pricing and sales

---

### 3. Unstructured Data (Web Scraping)
Source:
- Competitor e-commerce website

Format:
- HTML → CSV

Purpose:
- Extract competitor product pricing and market intelligence data

---

## Project Architecture

### Phase 1: Data Ingestion
- Download Excel datasets using Python
- Consume REST APIs using `requests`
- Scrape website data using `BeautifulSoup`

### Phase 2: Data Transformation
- Handle missing values
- Clean inconsistent formats
- Standardize currencies and prices
- Flatten nested JSON structures
- Prepare analytical datasets

### Phase 3: Data Modeling
- Build structured analytical models
- Create relationships between datasets
- Prepare fact and dimension tables

### Phase 4: Visualization
- Build interactive Power BI dashboards
- Generate pricing and sales insights
- Analyze competitor trends

---

## Tech Stack

- Python
- Pandas
- Power BI
- Git & GitHub
- REST APIs
- BeautifulSoup
- Jupyter Notebook
- VS Code

---

## Key Features

- Multi-source data ingestion
- ETL pipeline development
- API integration
- Web scraping automation
- Data cleaning and transformation
- Pricing intelligence analysis
- Currency exchange analysis
- Dashboard development
- Version control using GitHub

---

## Folder Structure

```plaintext
data_raw/
data_processed/
scripts/
notebooks/
powerbi/
docs/
README.md
```

---

## Current Progress

### Completed
- Project structure setup
- GitHub integration
- Multi-source ingestion pipeline
- Excel data ingestion
- API data ingestion
- Web scraping pipeline

### In Progress
- Data transformation pipeline
- Data modeling
- Power BI dashboard development

---

## Future Enhancements

- Automated pipeline scheduling
- Advanced pricing analytics
- Forecasting models
- Cloud deployment
- Real-time API ingestion

---

## Author

Neha Doda
