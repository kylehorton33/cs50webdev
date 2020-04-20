# Notes from Lecture 3

## Relational Databases

## Creata a database

What type of data?
- INTEGER
- DECIMAL
- SERIAL (automatically increase value)
- VARCHAR (variable length of characters, string)
- TIMESTAMP
- BOOLEAN
- ENUM (one of a finite number of discrete vars)

Constraints
- NOT NULL
- UNIQUE
- PRIMARY KEY
- DEFAULT
- CHECK

## Types of queries

- CREATE

- INSERT
- SELECT
SELECT * FROM flights
- UPDATE
UPDATE flights 
  SET duration = 430
  WHERE origin = 'New York'
  AND destination = 'London';
- DELETE
DELETE FROM flights
  WHERE destination = 'Tokyo';
 
# Additional Terms
- WHERE
- LIMIT
- ORDER BY
- CREATE INDEX


# Functions
- avg()
- count()
- min()
- max()
- sum()

## "Relational" Databases

Create a second table and link information together. Nested queries

## Security: SQL Injection

## SQL Transactions
- BEGIN
- COMMIT
- SQLAlchemy
