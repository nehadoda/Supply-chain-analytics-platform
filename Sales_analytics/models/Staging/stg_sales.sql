SELECT
    TRIM("Segment")                       AS segment,
    TRIM("Country")                       AS country,
    TRIM("Product")                       AS product,
    TRIM("Discount Band")                 AS discount_band,
    CAST("Units Sold" AS DOUBLE)          AS units_sold,
    CAST("Manufacturing Price" AS DOUBLE) AS manufacturing_price,
    CAST("Sale Price" AS DOUBLE)          AS sale_price,
    CAST("Gross Sales" AS DOUBLE)         AS gross_sales,
    CAST("Discounts" AS DOUBLE)           AS discounts,
    CAST(" Sales" AS DOUBLE)              AS net_sales,
    CAST("COGS" AS DOUBLE)                AS cogs,
    CAST("Profit" AS DOUBLE)              AS profit,
    CAST("Month Number" AS INTEGER)       AS month_number,
    TRIM("Month Name")                    AS month_name,
    CAST("Year" AS INTEGER)               AS year,
    MAKE_DATE(
        CAST("Year" AS INTEGER),
        CAST("Month Number" AS INTEGER),
        1
    )                                     AS sale_date
FROM {{ ref('raw_sales') }}
WHERE "Units Sold" IS NOT NULL