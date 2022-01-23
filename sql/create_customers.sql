CREATE TABLE IF NOT EXISTS customers (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NULL,
    first_name VARCHAR(45) NULL,
    last_name VARCHAR(45) NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(20) NULL,
    address_id INT NULL,
    notes TEXT NULL,
    created_by_id INT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NULL
);