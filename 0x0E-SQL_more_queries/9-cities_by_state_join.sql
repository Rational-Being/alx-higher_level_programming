-- lists table using join

SELECT cities_id, cities_name, states_name
FROM cities
INNER JOIN states ON cities.state_id=states.id
ORDER BY cities.id ASC;
