-- Create users table.
-- Check if users table exists and, if not, create it.
CREATE TABLE IF NOT EXISTS users (
        id INT NOT NULL AUTO_INCREMENT,
        email VARCHAR(255) NOT NULL UNIQUE,
        name VARCHAR(255),
        PRIMARY KEY (id)
);
