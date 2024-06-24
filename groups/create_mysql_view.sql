CREATE OR REPLACE  VIEW group_with_profile AS
SELECT 
	gp.id AS id, 
	gp.name_zh AS name_zh,
	g.id AS group_id, 
	g.name AS group_name
FROM auth_group g
LEFT JOIN group_profile gp ON g.id = gp.group_id;