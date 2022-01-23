CREATE TABLE IF NOT EXISTS order_items (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity_ordered INT NOT NULL,
    price_each FLOAT NOT NULL,
    discount FLOAT NULL,
    total_price FLOAT NULL,
    created_by_id INT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NULL
);