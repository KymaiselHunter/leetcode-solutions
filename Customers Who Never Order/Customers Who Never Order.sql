# Write your MySQL query statement below
Select name as Customers
    FROM Customers as c
    LEFT JOIN Orders as o
        on c.id = o.customerId
    WHERE o.id is NULL;