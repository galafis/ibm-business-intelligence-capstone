
-- Create Fact Tables
CREATE TABLE FactSales (
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

CREATE TABLE FactInventory (
    InventoryKey INT PRIMARY KEY,
    DateKey INT,
    ProductKey INT,
    QuantityOnHand INT,
    QuantityOnOrder INT,
    StockLevel VARCHAR(20),
    FOREIGN KEY (DateKey) REFERENCES DimDate(DateKey),
    FOREIGN KEY (ProductKey) REFERENCES DimProduct(ProductKey)
);
