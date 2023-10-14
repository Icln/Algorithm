with recursive t as(
    select 0 as h
    union all
    select h + 1
    from t
    where h < 23
), tmp as(
    select date_format(datetime, '%H') as HOUR, count(*) as c
    from animal_outs
    group by HOUR
    order by HOUR
)
    
select h, IFNULL(c, 0) as COUNT 
from t left join tmp on h = HOUR