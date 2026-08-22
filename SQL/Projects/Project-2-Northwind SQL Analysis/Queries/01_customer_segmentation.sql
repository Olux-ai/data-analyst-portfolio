SELECT Country, COUNT(*) CustomerCount 
FROM Customers
GROUP BY Country
ORDER BY CustomerCount DESC;

SELECT Country,COUNT(CustomerID) AS TotalCustomer
FROM Customers
GROUP BY Country
ORDER BY TotalCustomer DESC;

SELECT c.CustomerID, COUNT(o.OrderID) AS TotalOrders
FROM dbo.Customers c
INNER JOIN dbo.Orders o
  ON c.CustomerID = o.CustomerID
GROUP BY c.CustomerID
ORDER BY TotalOrders DESC;

SELECT c.CustomerID, SUM(od.UnitPrice * od.Quantity) AS TotalRevenue
FROM Customers AS c
INNER JOIN Orders AS o
ON c.CustomerID = o.CustomerID
INNER JOIN [Order Details] AS od
ON o.OrderID = od.OrderID
GROUP BY c.CustomerID
ORDER BY TotalRevenue DESC;

SELECT c.CustomerID, COUNT(*) AS TotalOrders
FROM Customers AS c
INNER JOIN Orders AS o
ON c.CustomerID = o.CustomerID
GROUP BY c.CustomerID
HAVING COUNT(*) > 1
ORDER BY TotalOrders DESC;