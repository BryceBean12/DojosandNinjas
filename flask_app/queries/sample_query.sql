-- This file is for testing our queries before using them in python

-- Makes query easier without having to specify schema for every table
USE dojos_ninjas_schema;


-- Base methods for CRUD
-- SELECT * FROM table_name;
-- INSERT INTO table_name (column_name_1, column_name_2) VALUES (column_value_1. column_value_2), (column_value_1. column_value_2), ...
-- UPDATE table_name SET column_name_1 = column_value_1, column_name_2 = column_value_2, ...
-- DELETE FROM table_name WHERE conditions

-- Base Methods for filtering
-- WHERE condition OR condition AND condition
-- ORDER BY condition DESC / ASC
-- GROUP BY column_name
-- LIMIT amount OFFSET amount

-- Base joins
-- One to One / One to Many
-- SELECT * FROM table_1 JOIN table_2 ON table_2.foreign_id = table_1.id
-- Many to Many
-- SELECT * FROM table_1 JOIN middle_table ON table_1.id = middle_table.foreign_id_1 JOIN table_2 ON table_2.id = middle_table.foreign_id_2

-- Your Query Here
-- INSERT INTO dojos (name) VALUES
-- ("Seattle"),
-- ("New York");

SELECT * FROM dojos;


-- INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES
-- ("Michael", "Mason", 24, 1),
-- ("John", "Smith", 21, 1),
-- ("Jake", "Jones", 18, 2);

-- SELECT * FROM ninjas;