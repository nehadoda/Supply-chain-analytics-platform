SELECT DISTINCT
    product
FROM {{ ref('stg_sales') }}
WHERE product IS NOT NULL