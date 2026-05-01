# Write your MySQL query statement below
SELECT 
    EMPLOYEE.name AS Employee
FROM Employee AS EMPLOYEE
INNER JOIN Employee AS MANAGER
ON 
    EMPLOYEE.managerId = MANAGER.id
WHERE
    EMPLOYEE.salary > MANAGER.salary;