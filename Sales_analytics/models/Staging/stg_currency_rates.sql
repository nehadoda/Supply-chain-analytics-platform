SELECT
    TRIM(base_code)                        AS base_code,
    TRIM(target_currency)                  AS target_currency,
    CAST(exchange_rate AS DOUBLE)          AS exchange_rate,
    TRIM(last_updated)                     AS last_updated_utc
FROM {{ ref('raw_currency_rates') }}
WHERE exchange_rate IS NOT NULL
  AND exchange_rate > 0