SELECT DISTINCT
    country
FROM {{ ref('stg_sales') }}
WHERE country IS NOT NULL