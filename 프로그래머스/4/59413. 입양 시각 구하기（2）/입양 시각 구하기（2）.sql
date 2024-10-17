with recursive tmp as(
    select 0 as hour
    union
    select hour + 1 as hour
    from tmp 
    where hour < 23
)
select t.hour as hour, count(hour(datetime)) as count
from tmp t left join ANIMAL_OUTS a on t.hour = hour(datetime)
group by t.hour