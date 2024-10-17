select distinct id, email, first_name, last_name
from developers d, skillcodes s
where d.skill_code & s.code = s.code and s.category = 'Front End'
order by id;