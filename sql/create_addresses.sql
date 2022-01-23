CREATE TABLE IF NOT EXISTS addresses (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    street_address varchar(120) not null,
    city varchar(45) not null,
    postal_zip varchar(45) not null,
    province_state varchar(45) not null,
    created_by_id INT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NULL
);