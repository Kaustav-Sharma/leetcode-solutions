-- Last updated: 22/10/2026, 6:22:39 pm
# Write your MySQL query statement below
SELECT 
    score, 
    DENSE_RANK() OVER (ORDER BY score DESC) AS "rank"
FROM 
    Scores;