# Part 5.A: Crear una nueva tabla 'favorite_foods'
sql_create_favorite_foods = """
CREATE TABLE favorite_foods (
  food_id integer,
  name text,
  vegetarian integer
);
"""

# Part 5.B: Modificar las tablas 'animals' y 'people'
sql_alter_tables_with_favorite_food = """
ALTER TABLE animals ADD COLUMN favorite_food_id integer;
ALTER TABLE people ADD COLUMN favorite_food_id integer;
"""

# Part 5.C: Escribir una consulta para seleccionar todas las mascotas vegetarianas
sql_select_all_vegetarian_pets = """
SELECT a.name, f.name
FROM animals AS a
JOIN favorite_foods AS f ON a.favorite_food_id = f.food_id
WHERE f.vegetarian = 1;
"""

