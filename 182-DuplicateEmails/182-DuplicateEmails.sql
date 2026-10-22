-- Last updated: 22/10/2026, 4:43:43 pm
# Write your MySQL query statement below
SELECT email FROM Person
GROUP BY email
HAVING COUNT(email) > 1;