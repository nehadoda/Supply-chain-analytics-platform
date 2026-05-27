SELECT
    s.segment,
    s.country,
    s.product,
    s.discount_band,
    s.units_sold,
    s.sale_price,
    s.gross_sales,
    s.discounts,
    s.net_sales,
    s.cogs,
    s.profit,
    s.month_name,
    s.month_number,
    s.year,
    s.sale_date,
    c.exchange_rate,
    c.target_currency,
    ROUND(s.net_sales * c.exchange_rate, 2)  AS net_sales_converted,
    ROUND(s.profit * c.exchange_rate, 2)     AS profit_converted
FROM {{ ref('stg_sales') }} s
LEFT JOIN {{ ref('stg_currency_rates') }} c
    ON c.target_currency IN ('GBP','EUR','CAD','AUD')