-- models/marts/fct_price_comparison.sql
SELECT
    s.product,
    s.segment,
    s.country,
    ROUND(AVG(s.sale_price), 2)          AS avg_our_price,
    ROUND(AVG(c.competitor_price_usd), 2) AS avg_competitor_price,
    ROUND(
        AVG(s.sale_price) - AVG(c.competitor_price_usd)
    , 2)                                  AS price_difference,
    CASE
        WHEN AVG(s.sale_price) > AVG(c.competitor_price_usd)
            THEN 'We Are More Expensive'
        WHEN AVG(s.sale_price) < AVG(c.competitor_price_usd)
            THEN 'We Are Cheaper'
        ELSE 'Same Price'
    END                                   AS price_position
FROM {{ ref('stg_sales') }} s
CROSS JOIN {{ ref('stg_competitor_prices') }} c
GROUP BY s.product, s.segment, s.country