# hive
CREATE EXTERNAL TABLE IF NOT EXISTS mapred_ext(
    tconst STRING,
    actors INT
)
    COMMENT 'mapred results'
    ROW FORMAT DELIMITED
    FIELDS TERMINATED BY '\t'
    STORED AS TEXTFILE
    location '/user/${USER}/mapred';

CREATE EXTERNAL TABLE IF NOT EXISTS mapred_orc(
    tconst STRING,
    actors INT
)
    COMMENT 'mapred results'
    STORED AS ORC
    location '/user/${USER}/mapred';

INSERT OVERWRITE TABLE mapred_orc
SELECT * FROM mapred_ext;

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
    location '/user/${USER}/basics';

CREATE EXTERNAL TABLE IF NOT EXISTS basics_orc(
    tconst STRING,
    genre STRING
)
    COMMENT 'movies informations'
    STORED AS ORC
    location '/user/${USER}/basics';

INSERT OVERWRITE TABLE basics_orc
SELECT tconst, genre
FROM basics_ext
LATERAL VIEW
EXPLODE(genres) AS genre;

WITH source AS (
    SELECT
        b.genre,
        b.tconst
        COALESCE(m.actors, 0) AS actors
    FROM basics_orc b LEFT OUTER JOIN mapred_orc m ON b.tconst = m.tconst
)
SELECT
    genre,
    COUNT(tconst) AS movies,
    SUM(actors)
FROM source
GROUP BY genre
ORDER BY SUM(actors) DESC
LIMIT 3;
