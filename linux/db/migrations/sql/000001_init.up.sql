CREATE TABLE surfline_spot (
    id INTEGER PRIMARY KEY,
    spot_id VARCHAR(255),
    name VARCHAR(255),
    location POINT
);


CREATE TABLE surfline_forecast (
    id INTEGER PRIMARY KEY,
    timestamp INTEGER,
    min INTEGER,
    max INTEGER,
    plus BOOLEAN,
    humanRelation VARCHAR(255),
    raw VARCHAR(255),
    optimalScore INTEGER,
    accurateRating BOOLEAN,
    realMin INTEGER,
    realMax INTEGER,
    comments VARCHAR(255)
);
