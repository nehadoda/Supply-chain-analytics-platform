-- models/marts/fct_profit_analysis.sql
SELECT
    product,
    segment,
    country,
    year,
    month_name,
    SUM(units_sold)                               AS total_units_sold,
    SUM(gross_sales)                              AS total_gross_sales,
    SUM(discounts)                                AS total_discounts,
    SUM(net_sales)                                AS total_net_sales,
    SUM(cogs)                                     AS total_cogs,
    SUM(profit)                                   AS total_profit,
    ROUND(SUM(profit) / NULLIF(SUM(net_sales), 0) * 100, 2) AS profit_margin_pct,
    CASE
        WHEN SUM(profit) / NULLIF(SUM(net_sales), 0) > 0.20
            THEN 'High Margin'
        WHEN SUM(profit) / NULLIF(SUM(net_sales), 0) > 0.10
            THEN 'Medium Margin'
        ELSE 'Low Margin'
    END                                           AS margin_category
FROM {{ ref('stg_sales') }}
GROUP BY product, segment, country, year, month_name