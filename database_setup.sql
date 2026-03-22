-- Drop tables if they exist to avoid errors on reruns
DROP TABLE IF EXISTS ordersdetails CASCADE;
DROP TABLE IF EXISTS orders CASCADE;
DROP TABLE IF EXISTS products CASCADE;
DROP TABLE IF EXISTS categories CASCADE;
DROP TABLE IF EXISTS suppliers CASCADE;
DROP TABLE IF EXISTS customers CASCADE;
DROP TABLE IF EXISTS employees CASCADE;
DROP TABLE IF EXISTS shippers CASCADE;

CREATE TABLE categories (
    CategoryID INT PRIMARY KEY,
    CategoryName VARCHAR(255) NOT NULL UNIQUE,
    Description TEXT
);

CREATE TABLE customers (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(255) NOT NULL,
    ContactName VARCHAR(255),
    Address VARCHAR(255),
    City VARCHAR(100),
    PostalCode VARCHAR(50),
    Country VARCHAR(100)
);

CREATE TABLE employees (
    EmployeeID INT PRIMARY KEY,
    LastName VARCHAR(255) NOT NULL,
    FirstName VARCHAR(255) NOT NULL,
    BirthDate TIMESTAMP,
    Photo VARCHAR(255),
    Notes TEXT
);

CREATE TABLE shippers (
    ShipperID INT PRIMARY KEY,
    ShipperName VARCHAR(255) NOT NULL,
    Phone VARCHAR(50)
);

CREATE TABLE suppliers (
    SupplierID INT PRIMARY KEY,
    SupplierName VARCHAR(255) NOT NULL,
    ContactName VARCHAR(255),
    Address VARCHAR(255),
    City VARCHAR(100),
    PostalCode VARCHAR(50),
    Country VARCHAR(100),
    Phone VARCHAR(50)
);

CREATE TABLE products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(255) NOT NULL,
    SupplierID INT,
    CategoryID INT,
    Unit VARCHAR(255),
    Price DECIMAL(10, 2),
    FOREIGN KEY (SupplierID) REFERENCES suppliers(SupplierID),
    FOREIGN KEY (CategoryID) REFERENCES categories(CategoryID)
);

CREATE TABLE orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    EmployeeID INT,
    OrderDate TIMESTAMP NOT NULL,
    ShipperID INT,
    FOREIGN KEY (CustomerID) REFERENCES customers(CustomerID),
    FOREIGN KEY (EmployeeID) REFERENCES employees(EmployeeID),
    FOREIGN KEY (ShipperID) REFERENCES shippers(ShipperID)
);

CREATE TABLE ordersdetails (
    OrderDetailID INT PRIMARY KEY,
    OrderID INT,
    ProductID INT,
    Quantity INT NOT NULL,
    FOREIGN KEY (OrderID) REFERENCES orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES products(ProductID)
);