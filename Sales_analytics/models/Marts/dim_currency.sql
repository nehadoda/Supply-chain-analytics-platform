SELECT DISTINCT
    target_currency,
    base_code
FROM {{ ref('stg_currency_rates') }}
WHERE target_currency IS NOT NULL