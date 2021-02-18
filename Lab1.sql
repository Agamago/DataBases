SELECT FirstName, LastName, Email
FROM Employee;

SELECT
*FROM Artist;

SELECT
*FROM Employee
WHERE Title like 'Manager';

SELECT min(Total), max(Total)
FROM  Invoice;

SELECT BillingAddress, BillingCity, BillingPostalCode, Total
FROM Invoice
WHERE BillingCountry = 'Germany';

SELECT BillingAddress, BillingCity, BillingCountry, BillingPostalCode, Total
FROM Invoice
WHERE Total < 25 and Total > 15;

SELECT distinct BillingCountry
FROM Invoice;

SELECT
*FROM Customer
WHERE Country != 'USA';

SELECT
*FROM Customer
WHERE Country = 'Brazil';

SELECT Name
From Track
Join InvoiceLine IL on Track.TrackId = IL.TrackId


