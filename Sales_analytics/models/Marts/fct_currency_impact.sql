-- models/marts/fct_currency_impact.sql
SELECT
    s.country,
    s.product,
    s.year,
    s.month_name,
    SUM(s.net_sales)                              AS revenue_in_usd,
    c.target_currency,
    c.exchange_rate,
    ROUND(SUM(s.net_sales) * c.exchange_rate, 2)  AS revenue_in_local_currency,
    ROUND(
        (SUM(s.net_sales) * c.exchange_rate) 
        - SUM(s.net_sales)
    , 2)                                          AS currency_impact_usd
FROM {{ ref('stg_sales') }} s
LEFT JOIN {{ ref('stg_currency_rates') }} c
    ON c.target_currency = CASE
        WHEN s.country = 'France'  THEN 'EUR'
        WHEN s.country = 'Germany' THEN 'EUR'
        WHEN s.country = 'Canada'  THEN 'CAD'
        WHEN s.country = 'Mexico'  THEN 'MXN'
        WHEN s.country = 'United States of America' THEN 'USD'
        ELSE 'USD'
    END
GROUP BY s.country, s.product, s.year, s.month_name,
         c.target_currency, c.exchange_rate