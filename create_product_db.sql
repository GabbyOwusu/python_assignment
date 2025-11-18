
-- 1) Create product table and insert 5 records
DROP TABLE IF EXISTS product;
CREATE TABLE product (
    id INT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    price DECIMAL(10,2) NOT NULL
);

INSERT INTO product (id, product_name, category, price) VALUES
(1, 'USB-C Cable', 'Electronics', 49.99),
(2, 'Wireless Headphones', 'Electronics', 199.99),
(3, 'Stapler', 'Office', 9.99),
(4, 'Air Fryer', 'Home', 150.00),
(5, 'Notebook Pack', 'Office', 24.50);

-- 2) Create sales table and insert 5 records
CREATE TABLE sales (
    id INT PRIMARY KEY,
    product_id INT NOT NULL,
    quantity_sold INT NOT NULL,
    sale_date DATE NOT NULL,
    total_price DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (product_id) REFERENCES product(id)
);

INSERT INTO sales (id, product_id, quantity_sold, sale_date, total_price) VALUES
(1, 2, 1, '2025-01-05', 199.99),
(2, 1, 3, '2025-01-06', 149.97),
(3, 3, 10, '2025-01-07', 99.90),
(4, 4, 1, '2025-01-08', 150.00),
(5, 5, 2, '2025-01-09', 49.00);

-- 3) Retrieve all data from product
SELECT * FROM product;

-- 4) Retrieve product_name and price from product table
SELECT product_name, price FROM product;

-- 5) Retrieve only 2 records from sales table
SELECT * FROM sales LIMIT 2;


-- 6) Retrieve sales that have total_price more than 100
SELECT * FROM sales WHERE total_price > 100;

-- 7) Retrieve products that have the same category (i.e. categories with more than one product)
SELECT * FROM product
WHERE category IN (
    SELECT category FROM product GROUP BY category HAVING COUNT(*) > 1
);

-- 8) Get the total number of products
SELECT COUNT(*) AS total_products FROM product;

-- 9) Get sum of total sales
SELECT SUM(total_price) AS total_sales FROM sales;

-- 10) Get avg of product price
SELECT AVG(price) AS avg_price FROM product;