SELECT
    row_to_json(meteo_data)
FROM
    meteo_data
ORDER BY
    "DT"
DESC 
LIMIT 
    :limit