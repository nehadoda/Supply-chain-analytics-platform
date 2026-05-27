SELECT
    TRIM(product_name)                AS product_name,
    CAST(
        REPLACE(
            REPLACE(competitor_price, '$', ''),
        ',', '')
        AS DOUBLE)                    AS competitor_price_usd,
    TRIM(description_snippet)         AS description_snippet,
    CURRENT_DATE                      AS scraped_date
FROM {{ ref('raw_competitor_prices') }}
WHERE competitor_price IS NOT NULL