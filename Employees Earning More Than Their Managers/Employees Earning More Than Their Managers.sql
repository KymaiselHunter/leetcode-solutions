# Write your MySQL query statement below
SELECT e.name as Employee 
    FROM Employee AS e 
    JOIN Employee AS m
        on e.managerId = m.id
        where e.salary > m.salary;