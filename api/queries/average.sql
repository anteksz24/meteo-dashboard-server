SELECT
    row_to_json(t)
FROM (
    SELECT
        date_bin(INTERVAL '1 minute' * :interval, "datetime", 'epoch') AS "datetime_bin",
        ROUND(AVG("air_temp_avg_1m")::NUMERIC, 1) AS "air_temp_avg_1m",
        ROUND(AVG("humidity_avg_1m")::NUMERIC, 0) AS "humidity_avg_1m",
        ROUND(AVG("dewpoint_avg_1m")::NUMERIC, 1) AS "dewpoint_avg_1m",
        ROUND(AVG("precipitation_sum_1h")::NUMERIC, 0) as "precipitation_sum_1h",
        ROUND(AVG("solar_rad_avg_1m")::NUMERIC, 0) AS "solar_rad_avg_1m",
        ROUND(AVG("sunshine_dur_1m")::NUMERIC, 0) AS "sunshine_dur_1m",
        ROUND(AVG("sunshine_dur_sum_1d")::NUMERIC, 0) AS "sunshine_dur_sum_1d",
        ROUND(AVG("air_temp_min_1d")::NUMERIC, 1) AS "air_temp_min_1d",
        ROUND(AVG("air_temp_max_1d")::NUMERIC, 1) AS "air_temp_max_1d",
        ROUND(AVG("humidity_min_1d")::NUMERIC, 0) AS "humidity_min_1d",
        ROUND(AVG("humidity_max_1d")::NUMERIC, 0) AS "humidity_max_1d",
        ROUND(AVG("air_temp_5cm_above_ground_avg_1m")::NUMERIC, 1) AS "air_temp_5cm_above_ground_avg_1m",
        ROUND(AVG("air_temp_surface_avg_1m")::NUMERIC, 1) AS "air_temp_surface_avg_1m",
        ROUND(AVG("ground_temp_5cm_avg_1m")::NUMERIC, 1) AS "ground_temp_5cm_avg_1m",
        ROUND(AVG("ground_temp_10cm_avg_1m")::NUMERIC, 1) AS "ground_temp_10cm_avg_1m",
        ROUND(AVG("ground_temp_20cm_avg_1m")::NUMERIC, 1) AS "ground_temp_20cm_avg_1m",
        ROUND(AVG("ground_temp_50cm_avg_1m")::NUMERIC, 1) AS "ground_temp_50cm_avg_1m",
        ROUND(AVG("ground_temp_100cm_avg_1m")::NUMERIC, 1) AS "ground_temp_100cm_avg_1m",
        ROUND(AVG("wind_direction_inst")::NUMERIC, 0) AS "wind_direction_inst",
        ROUND(AVG("wind_speed_inst")::NUMERIC, 1) AS "wind_speed_inst",
        ROUND(AVG("wind_direction_avg_2m")::NUMERIC, 0) AS "wind_direction_avg_2m",
        ROUND(AVG("wind_direction_max_2m")::NUMERIC, 0) AS "wind_direction_max_2m",
        ROUND(AVG("wind_direction_min_2m")::NUMERIC, 0) AS "wind_direction_min_2m",
        ROUND(AVG("wind_speed_avg_2m")::NUMERIC, 1) AS "wind_speed_avg_2m",
        ROUND(AVG("wind_speed_max_2m")::NUMERIC, 1) AS "wind_speed_max_2m",
        ROUND(AVG("wind_speed_min_2m")::NUMERIC, 1) AS "wind_speed_min_2m",
        ROUND(AVG("pressure_avg_1m")::NUMERIC, 1) AS "pressure_avg_1m",
        ROUND(AVG("pressure_adj_avg_1m")::NUMERIC, 1) AS "pressure_adj_avg_1m"
    FROM
        meteo_data
    WHERE
        datetime
	BETWEEN
		:start
	AND
		:end
    GROUP BY
        "datetime_bin"
    ORDER BY
        "datetime_bin"
) t;