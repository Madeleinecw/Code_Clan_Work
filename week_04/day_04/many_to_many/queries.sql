SELECT victims.*, zombies.name FROM victims 
INNER JOIN bitings ON victims.id = bitings.victim_id
-- SELECT * FROM victims LEFT JOIN bitings ON victims.id = bitings.victim_id;
INNER JOIN zombies ON bitings.id = zombies.id
WHERE bitings.zombie_id = 2;
