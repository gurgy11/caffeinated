CREATE TABLE IF NOT EXISTS orders (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NULL,
    payment_id INT NULL,
    shipped_date DATE NULL,
    delivered_date DATE NULL,
    shipping_address_id INT NULL,
    shipping_price FLOAT NULL,
    total_price FLOAT NULL,
    order_status VARCHAR(45) NULL,
    comments TEXT NULL,
    created_by_id INT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NULL
);