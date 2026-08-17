# Write your MySQL query statement below
Select Product.product_name ,Sales.year ,Sales.price from product inner Join sales on Product.product_id=Sales.product_id;