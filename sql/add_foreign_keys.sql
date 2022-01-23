ALTER TABLE addresses
ADD FOREIGN KEY (created_by_id) REFERENCES users(id);

ALTER TABLE users
ADD FOREIGN KEY (address_id) REFERENCES addresses(id);

ALTER TABLE brands
ADD FOREIGN KEY (created_by_id) REFERENCES users(id);

ALTER TABLE categories
ADD FOREIGN KEY (parent_id) REFERENCES categories(id);

ALTER TABLE categories
ADD FOREIGN KEY (created_by_id) REFERENCES users(id);

ALTER TABLE customers
ADD FOREIGN KEY (address_id) REFERENCES addresses(id);

ALTER TABLE customers
ADD FOREIGN KEY (created_by_id) REFERENCES users(id);

ALTER TABLE employees
ADD FOREIGN KEY (reports_to_id) REFERENCES employees(id);

ALTER TABLE employees
ADD FOREIGN KEY (created_by_id) REFERENCES users(id);

ALTER TABLE customers
ADD FOREIGN KEY (address_id) REFERENCES addresses(id);

ALTER TABLE suppliers
ADD FOREIGN KEY (created_by_id) REFERENCES users(id);

ALTER TABLE payments
ADD FOREIGN KEY (customer_id) REFERENCES customers(id);

ALTER TABLE payments
ADD FOREIGN KEY (created_by_id) REFERENCES users(id);

ALTER TABLE orders
ADD FOREIGN KEY (customer_id) REFERENCES customers(id);

ALTER TABLE orders
ADD FOREIGN KEY (payment_id) REFERENCES payments(id);

ALTER TABLE orders
ADD FOREIGN KEY (shipping_address_id) REFERENCES addresses(id);

ALTER TABLE orders
ADD FOREIGN KEY (created_by_id) REFERENCES orders(id);

ALTER TABLE products
ADD FOREIGN KEY (brand_id) REFERENCES brands(id);

ALTER TABLE products
ADD FOREIGN KEY (category_id) REFERENCES categories(id);

ALTER TABLE products
ADD FOREIGN KEY (supplier_id) REFERENCES suppliers(id);

ALTER TABLE products
ADD FOREIGN KEY (created_by_id) REFERENCES users(id);

ALTER TABLE order_items
ADD FOREIGN KEY (order_id) REFERENCES orders(id);

ALTER TABLE order_items
ADD FOREIGN KEY (product_id) REFERENCES products(id);

ALTER TABLE order_items
ADD FOREIGN KEY (created_by_id) REFERENCES orders(id);