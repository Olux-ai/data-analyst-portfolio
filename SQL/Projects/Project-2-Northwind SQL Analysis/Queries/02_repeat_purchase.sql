SELECT c.CustomerID, c.CompanyName, COUNT(o.OrderID) AS TotalPurchases
FROM Customers AS c
LEFT JOIN Orders AS o
ON c.CustomerID = o.CustomerID
GROUP BY c.CustomerID, c.CompanyName
HAVING COUNT(o.OrderID) > 1
ORDER BY TotalPurchases DESC;

SELECT c.CustomerID, c.CompanyName, COUNT(o.OrderID) AS TotalOrders
FROM Customers AS c
INNER JOIN Orders AS o
ON c.CustomerID = o.CustomerID
GROUP BY c.CustomerID, c.CompanyName
ORDER BY TotalOrders DESC;