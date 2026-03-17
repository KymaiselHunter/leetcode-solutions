# Write your MySQL query statement below
Select firstName, lastName, city, state FROM
    Person LEFT JOIN Address
        on Person.personId = Address.personId;