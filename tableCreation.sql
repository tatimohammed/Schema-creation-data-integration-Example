----------------------------------------------------------------------------------------------------------------
-- Note:                                                                                                      --
--      - When you are creating a database always start with the tables with no constraints (Foreign keys).   --
----------------------------------------------------------------------------------------------------------------

-- Creating the user table
CREATE TABLE User (
    user_id INT PRIMARY KEY,
    username VARCHAR(100),
    email VARCHAR(100),
    password VARCHAR(100)
);

-- Creating the product table
CREATE TABLE Product (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    price DECIMAL(10,2)
);

-- Creating the order table
CREATE TABLE Order (
    order_id INT PRIMARY KEY,
    user_id INT,
    product_id INT,
    quantity INT,
    order_date DATE,
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    FOREIGN KEY (product_id) REFERENCES Product(product_id)
);
