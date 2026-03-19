SELECT
    row_to_json(meteo_data)
FROM
    meteo_data
WHERE
    "DT"
BETWEEN
    :start
AND
    :end
ORDER BY
    "DT"
ASC