-- Please add the proper SQL query to follow the instructions below  

-- 0) Select ecommerce as your default database 
USE ecommerce;


-- 1) Show the PK, name, and quantity per unit from all products
select ProductID, ProductName, QuantityPerUnit from products p;


-- 2) Show the number of products ever available in our stores
select distinct count(ProductID) from products; 


-- 3) Show the number of products with more orders than stock
select distinct count(ProductID) from products where UnitsOnOrder>UnitsInStock;


-- 4) List all products available in the store (in stock) and order them alphabetically from a to z 
-- Show just the first ten products 
select productname from products where unitsinstock > 0 order by productname limit 10;


-- 5) Create a new table called scustomers with all the customers from a country that starts with the letter S
create table scustomers as
select customerid from customers where country like "%S";


-- 6) Delete the previously created table
drop table scustomers;

-- 7) Show how many different countries our customers come from
select distinct count(country) from customers;


-- 8) Show how many customers are from Mexico, Argentina, or Brazil 
--  whose contact title is  Sales Representative or a Sales Manager
select count(customerid) 
from customers 
where contacttitle in ('Sales Representative', 'Sales Manager') and country in ('Brazil', 'Argentina', 'Mexico');


-- 9) Show the number of employees that were 50 years old or more 
--  as at 2014-10-06 (you will probably need to use the DATE_FORMAT function) 
select count(employeeID) from employees where TIMESTAMPDIFF(YEAR, birthdate, '2014-10-06') >= 50;


-- 10) Show the number of customers with a Spanish or British common surname
--  (a surname that ends with -on or -ez)
select count(customerid) from customers where contactname like "%on" or contactname like "%ez";



