
-- Create Data Warehouse Schema
CREATE DATABASE IF NOT EXISTS BusinessIntelligenceDW;
USE BusinessIntelligenceDW;

-- Dimension Tables
CREATE TABLE IF NOT EXISTS DimDate (
    DateKey INT PRIMARY KEY,
    FullDate DATE,
    DayOfWeek VARCHAR(10),
    DayOfMonth INT,
    Month INT,
    MonthName VARCHAR(10),
    Quarter INT,
    Year INT,
    IsWeekend BIT
);

CREATE TABLE IF NOT EXISTS DimCustomer (
    CustomerKey INT PRIMARY KEY,
    CustomerID VARCHAR(20),
    CustomerName VARCHAR(100),
    CustomerType VARCHAR(50),
    CustomerSegment VARCHAR(50),
    Country VARCHAR(50),
    Region VARCHAR(50),
    City VARCHAR(50),
    StartDate DATE,
    EndDate DATE,
    IsCurrent BIT
);

CREATE TABLE IF NOT EXISTS DimProduct (
    ProductKey INT PRIMARY KEY,
    ProductID VARCHAR(20),
    ProductName VARCHAR(100),
    ProductCategory VARCHAR(50),
    ProductSubcategory VARCHAR(50),
    Brand VARCHAR(50),
    UnitPrice DECIMAL(10,2),
    StartDate DATE,
    EndDate DATE,
    IsCurrent BIT
);

-- Fact Tables
CREATE TABLE IF NOT EXISTS FactSales (
    SalesKey INT PRIMARY KEY,
    DateKey INT,
    CustomerKey INT,
    ProductKey INT,
    SalesAmount DECIMAL(12,2),
    Quantity INT,
    Discount DECIMAL(5,2),
    Profit DECIMAL(12,2),
    FOREIGN KEY (DateKey) REFERENCES DimDate(DateKey),
    FOREIGN KEY (CustomerKey) REFERENCES DimCustomer(CustomerKey),
    FOREIGN KEY (ProductKey) REFERENCES DimProduct(ProductKey)
);

CREATE TABLE IF NOT EXISTS FactInventory (
    InventoryKey INT PRIMARY KEY,
    DateKey INT,
    ProductKey INT,
    QuantityOnHand INT,
    QuantityOnOrder INT,
    StockLevel VARCHAR(20),
    FOREIGN KEY (DateKey) REFERENCES DimDate(DateKey),
    FOREIGN KEY (ProductKey) REFERENCES DimProduct(ProductKey)
);

-- Aggregate Tables
CREATE TABLE IF NOT EXISTS AggSalesByMonth (
    MonthKey INT,
    ProductCategory VARCHAR(50),
    TotalSales DECIMAL(15,2),
    TotalQuantity INT,
    TotalProfit DECIMAL(15,2),
    PRIMARY KEY (MonthKey, ProductCategory)
);

CREATE TABLE IF NOT EXISTS AggCustomerSegment (
    CustomerSegment VARCHAR(50),
    Year INT,
    Quarter INT,
    TotalSales DECIMAL(15,2),
    CustomerCount INT,
    AvgSalesPerCustomer DECIMAL(12,2),
    PRIMARY KEY (CustomerSegment, Year, Quarter)
);
