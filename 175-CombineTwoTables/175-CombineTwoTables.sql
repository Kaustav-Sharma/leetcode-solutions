-- Last updated: 22/10/2026, 6:20:02 pm
# Write your MySQL query statement below
SELECT 
    Person.firstName, 
    Person.lastName, 
    Address.city, 
    Address.state
FROM 
    Person
LEFT JOIN 
    Address ON Person.personId = Address.personId;