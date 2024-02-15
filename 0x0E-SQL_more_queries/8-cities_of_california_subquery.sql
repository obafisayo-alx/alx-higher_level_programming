USE hbtn_0d_usa;

-- Find the state_id for California
SET @state_id = (SELECT id FROM states WHERE name = 'California');

-- Select cities of California
SELECT *
FROM cities
WHERE state_id = @state_id
ORDER BY id ASC;
