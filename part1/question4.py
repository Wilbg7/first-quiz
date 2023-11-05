import pets_db

# Part 4.A: Consulta SQL para seleccionar las mascotas sin propietario
sql_pets_owned_by_nobody = """
SELECT a.name, a.species, a.age
FROM animals AS a
LEFT JOIN people_animals AS pa ON a.animal_id = pa.pet_id
WHERE pa.owner_id IS NULL;
"""

# Part 4.B: Consulta SQL para calcular el número de mascotas más viejas que sus propietarios
sql_pets_older_than_owner = """
SELECT COUNT(*)
FROM animals AS a
JOIN people_animals AS pa ON a.animal_id = pa.pet_id
JOIN people AS p ON pa.owner_id = p.person_id
WHERE a.age > p.age;
"""

# Part 4.C: BONUS CHALLENGE: Consulta SQL para seleccionar las mascotas propiedad de Bessie y nadie más
sql_only_owned_by_bessie = """
SELECT p.name AS person_name, a.name AS pet_name, a.species
FROM people_animals AS pa
JOIN people AS p ON pa.owner_id = p.person_id
JOIN animals AS a ON pa.pet_id = a.animal_id
WHERE p.name = 'bessie'
AND NOT EXISTS (
  SELECT 1
  FROM people_animals AS pa2
  WHERE pa2.pet_id = a.animal_id
  AND pa2.owner_id <> p.person_id
);
"""
