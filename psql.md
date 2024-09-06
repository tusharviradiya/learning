psql -h localhost -U postgres -d postgres -p 5432
\l : list database
\c dbname : change database
\dt
\du : list user 

CREATE DATABASE db_name; 
DROP DATABASE test_db;

psql -U postgres -h localhost -d monty_mtr < /home/tushar/Downloads/monty_test_4_06_2024.sql //for take dump in db
pg_dump -U postgres -h localhost -d monty_mtr > /home/tushar/Downloads/monty_test_4_06_2024.sql //for creating dump file
psql -U postgres -h localhost -d monty_mtr -t monty_dailystats < /home/tushar/Downloads/dailystats.sql

SELECT COUNT(*) FROM monty_reading;

SELECT COUNT(*) 
FROM monty_reading 
WHERE heap_id = 2456 
AND monty_device_id = 1175;

DELETE FROM monty_reading
WHERE heap_id = 2456
AND monty_device_id = 1175
AND id NOT IN (
    SELECT id FROM monty_reading
    WHERE heap_id = 2456
    AND monty_device_id = 1175
    ORDER BY datetime DESC
    LIMIT 10000
);

DELETE FROM monty_reading
WHERE heap_id = 2456
AND monty_device_id = 1175;

