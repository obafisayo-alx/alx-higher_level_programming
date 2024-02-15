USE hbtn_0d_2;

-- Check if the table exists
SELECT COUNT(*) INTO @table_exists
FROM information_schema.TABLES
WHERE TABLE_SCHEMA = 'hbtn_0d_2' AND TABLE_NAME = 'force_name';

-- Create table if it doesn't exist
SET @sql = IF(@table_exists = 0,
    "CREATE TABLE force_name (
        id INT,
        name VARCHAR(256) NOT NULL
    );",
    "SELECT 'Table already exists';"
);

-- Execute SQL statement
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
