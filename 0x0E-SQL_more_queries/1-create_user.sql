-- Check if the user exists
SELECT COUNT(*) INTO @user_exists
FROM mysql.user
WHERE User = 'user_0d_1' AND Host = 'localhost';

-- Create user and grant privileges if it doesn't exist
SET @sql = IF(@user_exists = 0,
    "CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd'; GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;",
    "SELECT 'User already exists';"
);

-- Execute SQL statement
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
