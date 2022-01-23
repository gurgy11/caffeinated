CREATE TABLE IF NOT EXISTS products (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    brand_id INT NULL,
    title VARCHAR(120) NOT NULL,
    category_id INT NULL,
    details TEXT NULL,
    price FLOAT NULL,
    quantity INT NULL,
    supplier_id INT NULL,
    created_by_id INT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NULL
);