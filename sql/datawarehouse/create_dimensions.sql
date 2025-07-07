
-- Create Dimension Tables
CREATE TABLE DimDate (
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

CREATE TABLE DimCustomer (
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

CREATE TABLE DimProduct (
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
