SELECT
    row_to_json(meteo_data)
FROM
    meteo_data
WHERE
    "datetime"
BETWEEN
    :start
AND
    :end
ORDER BY
    "datetime"
ASC