CREATE TABLE IF NOT EXISTS template (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    created_by_id INT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NULL
);