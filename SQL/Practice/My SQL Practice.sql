USE Northwind;
GO

SELECT name
FROM sys.tables
ORDER BY name;
USE Northwind;
GO

SELECT TOP 10 *
FROM Customers;
SELECT
    Country,
    COUNT(*) AS CustomerCount
FROM Customers
GROUP BY Country
ORDER BY CustomerCount DESC;

SELECT TOP 10 *
FROM Orders

SELECT ShipCountry,
COUNT(*) AS NumberOfOrders
FROM orders
GROUP BY ShipCountry
HAVING COUNT(*) > 20
ORDER BY NumberOfOrders DESC;

SELECT ShipCountry, COUNT(*) AS OrderCount
FROM Orders
GROUP BY ShipCountry
HAVING COUNT(*) > 10
ORDER BY OrderCount DESC;

SELECT ShipCountry, COUNT(*) AS OrderCount, AVG(Freight) AS AverageFreight
FROM Orders
GROUP BY ShipCountry
HAVING COUNT(*) > 10
ORDER BY OrderCount DESC;

SELECT ProductID, 
SUM(Quantity) AS TotalQuantity
FROM [Order Details]
GROUP BY ProductID
HAVING SUM(Quantity) > 100
ORDER BY TotalQuantity DESC;

SELECT ProductID, SUM(UnitPrice * Quantity) AS TotalSales
FROM [Order Details]
GROUP BY ProductID
HAVING SUM(UnitPrice * Quantity) > 10000
ORDER BY TotalSales DESC;

SELECT ShipCountry, MIN(Freight) AS MinFreight, MAX(Freight) AS MaxFreight
FROM Orders
GROUP BY ShipCountry
ORDER BY MaxFreight DESC;

SELECT Categories.CategoryName, COUNT(*) AS OrderLine, SUM(Quantity) AS TotalQuantity, SUM(UnitPrice * Quantity) AS TotalSales,AVG(UnitPrice) AS AvgUnitPrice
FROM Products
INNER JOIN Categories
ON Products.CategoryID = Categories.CategoryID
INNER JOIN [Order Details]
ON Products.ProductID = [Order Details].ProductID
GROUP BY Categories.CategoryName
HAVING SUM(UnitPrice * Quantity) > 10000
ORDER BY TotalSales DESC;