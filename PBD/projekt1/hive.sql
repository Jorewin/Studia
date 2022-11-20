-- mapred
CREATE EXTERNAL TABLE IF NOT EXISTS mapred_ext(
    tconst STRING,
    actors INT
)
COMMENT 'mapred results'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS SEQUENCEFILE
LOCATION '${hivevar:input_dir3}';

-- basics
CREATE EXTERNAL TABLE IF NOT EXISTS basics_ext(
    tconst STRING,
    titleType STRING,
    primaryTitle STRING,
    originalTitle STRING,
    isAdult STRING,
    startYear STRING,
    endYear STRING,
    runtimeMinutes INT,
    genres ARRAY<STRING>
)
COMMENT 'movies informations'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
COLLECTION ITEMS TERMINATED BY ','
NULL DEFINED AS '\\N'
STORED AS TEXTFILE
location '${hivevar:input_dir4}';

-- execution
ADD JAR /usr/lib/hive/lib/hive-hcatalog-core.jar;

CREATE EXTERNAL TABLE IF NOT EXISTS results_ext(
    genre STRING,
    movies INT,
    actors INT
)
COMMENT 'project no. 1 results'
ROW FORMAT SERDE 'org.apache.hive.hcatalog.data.JsonSerDe'
STORED AS TEXTFILE
LOCATION '${hivevar:output_dir6}';

WITH
    basics AS (
        SELECT
            genre,
            tconst
        FROM basics_ext
        LATERAL VIEW EXPLODE(COALESCE(genres, ARRAY('Not specified'))) genres_exploded AS genre
        WHERE
            tconst != 'tconst' AND
            titleType = 'movie'
    ),
    source AS (
        SELECT
            b.genre,
            b.tconst,
            COALESCE(m.actors, 0) AS actors_per_movie
        FROM basics b LEFT OUTER JOIN mapred_ext m ON b.tconst = m.tconst
    )
INSERT INTO results_ext
SELECT
    genre,
    COUNT(tconst) AS movies,
    SUM(actors_per_movie) AS actors
FROM source
GROUP BY genre
ORDER BY actors DESC
LIMIT 3;

-- cleanup
DROP TABLE mapred_ext;
DROP TABLE basics_ext;
DROP TABLE results_ext;
