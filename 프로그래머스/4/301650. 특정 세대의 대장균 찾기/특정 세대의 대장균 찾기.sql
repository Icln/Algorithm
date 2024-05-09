with recursive tree as (
    select  ID, PARENT_ID, 1 as level
    from ECOLI_DATA
    where PARENT_ID is null

    union 

    select c.ID, c.PARENT_ID, t.level + 1 
    from ECOLI_DATA as c join tree as t on c.PARENT_ID = t.ID
)

select id
from tree
group by id
having max(level) = 3
order by id

