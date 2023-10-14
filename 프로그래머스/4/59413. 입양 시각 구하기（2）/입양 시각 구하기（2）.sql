with recursive tmp as(
    select 0 as h
    union all
    select h + 1
    from tmp
    where h < 23
)
select h, IFNULL(c, 0) as COUNT 
from tmp 
left join (
    select date_format(datetime, '%H') as HOUR, count(*) as c
    from animal_outs
    group by HOUR
    order by HOUR) a
on h = HOUR