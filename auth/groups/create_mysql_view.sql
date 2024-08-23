CREATE OR REPLACE  VIEW group_with_profile AS
SELECT 
	gp.id AS id, 
	gp.name_zh AS name_zh,
	gp.is_deleted AS is_deleted, 
	g.name AS name
FROM auth_group g
LEFT JOIN group_profile gp ON g.id = gp.group_id;