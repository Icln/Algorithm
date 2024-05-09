select ID, EMAIL, FIRST_NAME, LAST_NAME
from DEVELOPER_INFOS
where 'Python' in (SKILL_1, SKILL_2, SKILL_3)
order by id