select e.id, count(d.id) as child_count
from ECOLI_DATA e left outer join ECOLI_DATA d on e.id = d.parent_id
group by e.id