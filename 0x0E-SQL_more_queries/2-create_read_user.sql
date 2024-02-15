-- Check if the database exists
SELECT COUNT(*) INTO @db_exists
FROM information_schema.SCHEMATA
WHERE SCHEMA_NAME = 'hbtn_0d_2';

-- Create database if it doesn't exist
SET @sql_db = IF(@db_exists = 0,
    "CREATE DATABASE hbtn_0d_2;",
    "SELECT 'Database already exists';"
);

-- Execute SQL statement for creating the database
PREPARE stmt_db FROM @sql_db;
EXECUTE stmt_db;
DEALLOCATE PREPARE stmt_db;

-- Check if the user exists
SELECT COUNT(*) INTO @user_exists
FROM mysql.user
WHERE User = 'user_0d_2' AND Host = 'localhost';

-- Create user if it doesn't exist
SET @sql_user = IF(@user_exists = 0,
    "CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';",
    "SELECT 'User already exists';"
);

-- Execute SQL statement for creating the user
PREPARE stmt_user FROM @sql_user;
EXECUTE stmt_user;
DEALLOCATE PREPARE stmt_user;

-- Grant SELECT privilege on the database
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
