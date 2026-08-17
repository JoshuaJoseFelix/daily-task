# Write your MySQL query statement below
Select name as Customers from Customers c Left Join orders on c.id = customerId 
where customerId is null;