
-- Please add the proper SQL query to follow the instructions below  
USE musicstore;
-- 1.Show the Number of tracks whose composer is F. Baltes
-- (Note: there can be more than one composers for each track)
SELECT count(trackid)
FROM track t 
WHERE composer REGEXP 'F. Baltes';

-- 2.Show the Number of invoices, and the number of invoices with a total amount =0.99 in the same query
-- (Hint: you can use CASE WHEN)
SELECT count(invoiceid) as CountInvoice, sum(case when total = 0.99 then 1 else 0 end) as SpecialCount 
FROM invoice i;

-- 3.Show the album title and artist name of the first five albums sorted alphabetically
SELECT x.Title, y.Name 
from Album x 
inner join artist y on x.artistid=y.artistid 
order by x.title, y.Name
limit 5; 


-- 4.Show the Id, first name, and last name of the 10 first customers 
-- alphabetically ordered. Include the id, first name and last name 
-- of their support representative (employee)
 SELECT c.CustomerId, c.FirstName, c.LastName, e.employeeid, e.FirstName, e.LastName 
 from customer c 
 inner join employee e 
 on c.supportRepId = e.employeeId 
 order by c.LastName, c.FirstName
 Limit 10;


-- 5.Show the Track name, duration, album title, artist name,
--  media name, and genre name for the five longest tracks
SELECT t.Name as TrackName, t.Milliseconds as Duration, a.title as Album, x.name as Artist, g.name as Genre, m.name as Mediatype 
from Track t 
inner join album a on t.albumid = a.albumid 
inner join artist x on a.artistid = x.artistid 
inner join genre g on t.genreid = g.genreid
inner join mediatype m on t.mediatypeid = m.mediatypeid
order by t.milliseconds desc 
limit 5;


-- 6.Show the Five most expensive albums
--  (Those with the highest cumulated unit price)
--  together with the average price per track
select a.title as Album, sum(t.unitprice) as CumulatedUnitPrice, avg(t.unitprice) as AvgUnitPrice
from track t
inner join album a on t.albumid = a.albumid
group by t.albumid
order by CumulatedUnitPrice desc
limit 5;


-- 7. Show the Five most expensive albums
--  (Those with the highest cumulated unit price)
-- but only if the average price per track is above 1
select Album as Title
from ( 
	select a.title as Album, sum(t.unitprice) as CumulatedUnitPrice, avg(t.unitprice) as AvgUnitPrice
	from track t
	inner join album a on t.albumid = a.albumid
	group by t.albumid
	order by CumulatedUnitPrice desc) as priced_albums
where AvgUnitPrice > 1
limit 5;


-- 8.Show the album Id and number of different genres
-- for those albums with more than one genre
-- (tracks contained in an album must be from at least two different genres)
-- Show the result sorted by the number of different genres from the most to the least eclectic 

select id, NumGenres
from (
	select a.albumid as id, count(distinct genreid) as NumGenres
	from track t
	inner join album a on t.albumid = a.albumid
	group by t.albumid) as AlbumGenres
where NumGenres > 1
order by NumGenres desc;

-- 9.Show the total number of albums that you get from the previous result (hint: use a nested query)
select count(id) as CountAlbums
from (
	select a.albumid as id, count(distinct genreid) as NumGenres
	from track t
	inner join album a on t.albumid = a.albumid
	group by t.albumid) as AlbumGenres
where NumGenres > 1;


-- 10.Check that the total amount of money in each invoice
-- is equal to the sum of unit price x quantity
-- of its invoice lines.
select case when sum(invln.PriceTimesQuantity != i.total) = 0 then "All good!" else "They don't match!" end
from (
	select invoiceid, sum(unitprice*quantity) as PriceTimesQuantity
	from invoiceline il
	group by invoiceid) InvLn
inner join invoice i on i.invoiceid = InvLn.invoiceid;

-- 11.We are interested in those employees whose customers have generated 
-- the highest amount of invoices 
-- Show first_name, last_name, and total amount generated 

select e.firstname, e.lastname, count(distinct i.invoiceid) as Quantity
from invoice i
	inner join invoiceline il on i.invoiceid = il.invoiceid
	inner join customer c on i.customerid = c.customerid
	inner join employee e on c.supportrepid = e.employeeid
group by e.employeeid
order by Quantity desc;



-- 12.Show the following values: Average expense per customer, average expense per invoice, 
-- and average invoices per customer.
-- Consider just active customers (customers that generated at least one invoice)
SELECT AVG(TotalExpensePerCustomer) AS AvgExpensePerCustomer,
    AVG(TotalExpensePerInvoice) AS AvgExpensePerInvoice,
    AVG(NumInvoicesPerCustomer) AS AvgInvoicesPerCustomer
FROM (
    SELECT
        c.CustomerId,
        SUM(i.Total) AS TotalExpensePerCustomer,
        AVG(i.Total) AS TotalExpensePerInvoice,
        COUNT(DISTINCT i.InvoiceId) AS NumInvoicesPerCustomer
    FROM Customer c
    LEFT JOIN Invoice i ON c.CustomerId = i.CustomerId
    WHERE i.CustomerId IS NOT NULL
    GROUP BY c.CustomerId
) AS CustomerStats;


-- 13.We want to know the number of customers that are above the average expense level per customer. (how many?)
with CustomerExpense as (
    select
        c.CustomerId,
        SUM(i.Total) AS TotalExpensePerCustomer
    from Customer c
    left join Invoice i ON c.CustomerId = i.CustomerId
    where i.CustomerId IS NOT NULL -- Consider only active customers
    group by c.CustomerId
)

SELECT COUNT(*) AS NumCustomersAboveAverage
FROM CustomerExpense
WHERE TotalExpensePerCustomer > (SELECT AVG(TotalExpensePerCustomer) FROM CustomerExpense);

-- 14.We want to know who is the most purchased artist (considering the number of purchased tracks), 
-- who is the most profitable artist (considering the total amount of money generated).
-- and who is the most listened artist (considering purchased song minutes).
-- Show the results in 3 rows in the following format: 
-- ArtistName, Concept('Total Quantity','Total Amount','Total Time (in seconds)'), Value
-- (hint:use the UNION statement)
(
SELECT
    a.Name AS ArtistName,
    'Total Quantity' AS Concept,
    SUM(il.Quantity) AS Value
FROM Artist a
INNER JOIN Album al ON a.ArtistId = al.ArtistId
INNER JOIN Track t ON al.AlbumId = t.AlbumId
INNER JOIN InvoiceLine il ON t.TrackId = il.TrackId
GROUP BY a.ArtistId
ORDER BY Value DESC
LIMIT 1)

union
-- Most Profitable Artist
(SELECT
    a.Name AS ArtistName,
    'Total Amount' AS Concept,
    SUM(il.UnitPrice * il.Quantity) AS Value
FROM Artist a
INNER JOIN Album al ON a.ArtistId = al.ArtistId
INNER JOIN Track t ON al.AlbumId = t.AlbumId
INNER JOIN InvoiceLine il ON t.TrackId = il.TrackId
GROUP BY a.ArtistId
ORDER BY Value DESC
LIMIT 1)

union

-- Most Listened Artist
(SELECT
    a.Name AS ArtistName,
    'Total Time (in seconds)' AS Concept,
    SUM(t.Milliseconds / 1000) AS Value
FROM Artist a
INNER JOIN Album al ON a.ArtistId = al.ArtistId
INNER JOIN Track t ON al.AlbumId = t.AlbumId
INNER JOIN InvoiceLine il ON t.TrackId = il.TrackId
GROUP BY a.ArtistId
ORDER BY Value DESC
LIMIT 1);

