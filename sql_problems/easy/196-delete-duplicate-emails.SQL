# Write your MySQL query statement below
DELETE Person 
FROM Person, Person as Reference
WHERE Person.email = Reference.email AND Person.id > Reference.id