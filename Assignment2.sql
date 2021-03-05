/*
(1) Create a table Player with the following attributes.
You will also define what the data types are going to be.
 */

 CREATE TABLE Player (
    pID  SMALLINT UNSIGNED NOT NULL,
    Name VARCHAR(60) NOT NULL,
    teamName VARCHAR(60),
    PRIMARY KEY (pId)
 );
/*
 (2) Alter the Player table to add a new column, age
 */
ALTER TABLE Player
ADD COLUMN age TINYINT;

/*
 (3) Insert the following tuples into the table:
 a.(1,’Player 1’, ‘Team A’, 23)
 b.(2,’Player 2’, ‘Team A’)
 c.(3,’Player 3’, ‘Team B’, 28)
 d.(4,’Player 4’, ‘Team B’)
 */
 INSERT INTO Player
 VALUES (1,'Player1','Team A', 23),
        (2,'Player2','Team A', NULL),
        (3,'Player3','Team B', 28),
        (4,'Player4','Team B', NULL);

/*
 (4) Update the table to delete Player 2’s record from it.
 */
DELETE FROM Player
WHERE Name = 'Player2';

/*
 (5) Update the table to set age = 25 for tuples where age attribute is NULL.
 */
UPDATE Player
SET age = 25
WHERE age is null ;

/*
 (6) Write a query to return the number of tuples and average age from the Player table.
 */
SELECT AVG(age)
FROM Player AS '# of Records & Average Age'
UNION
SELECT COUNT(*)
FROM Player;
/*
 (7) Drop the player table
 */
 DROP TABLE Player;

/*
 ----------------------------------------------------------------------------------
 */
 
/*
 (8) Write a query to return the average Total of invoices where the billing country is Brazil.
 */

SELECT AVG(Total) AS 'AVG Cost in Brazil'
FROM Invoice
WHERE BillingCountry = 'Brazil';

/*
 (9)Write a query to return the average Total per billing city of invoices where the billing country is Brazil.
 */
SELECT AVG(Total), BillingCity
FROM Invoice
WHERE BillingCountry = 'Brazil'
GROUP BY BillingCity;

/*
 (10) Write a query to return the names of all albums which have a more than 20 tracks.
 */
 SELECT Title
 FROM Album
 INNER JOIN Track T on Album.AlbumId = T.AlbumId
 GROUP BY Title
 HAVING COUNT(Title) > 20;
/*
 (11) Write a query to show how many invoices were processed in the year 2010.
 */
SELECT COUNT(InvoiceDate)
From Invoice
WHERE InvoiceDate LIKE '%2010%';

/*
 (12) Write a query to answer how many distinct billing cities there are per each billing country.
 */
SELECT DISTINCT COUNT(BillingCity) AS 'Number of Cities', BillingCountry
FROM Invoice
GROUP BY BillingCountry;

/*
 (13) Write a query to show the album title, track name, and media type name for each record.
 */
SELECT Album.Title , T.Name , MT.Name
FROM Album
INNER JOIN Track T on Album.AlbumId = T.AlbumId
INNER JOIN MediaType MT on T.MediaTypeId = MT.MediaTypeId;

/*
 (14) Write a query to find how many sales(invoice count)did Jane Peacock make as a support representative.
 In the Customers table, you will find that SupportRepId maps to anemployeeID in the Employees table that you can use.
 I recommend using a subquery for this.
 */
SELECT COUNT(*)
FROM Invoice
INNER JOIN Customer C on Invoice.CustomerId = C.CustomerId
INNER JOIN Employee E on C.SupportRepId = E.EmployeeId
WHERE E.EmployeeId = 3;
