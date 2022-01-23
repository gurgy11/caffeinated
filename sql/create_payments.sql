CREATE TABLE IF NOT EXISTS payments (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NULL,
    payment_type VARCHAR(45) NOT NULL,
    amount FLOAT NOT NULL,
    details TEXT NULL,
    created_by_id INT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NULL
);