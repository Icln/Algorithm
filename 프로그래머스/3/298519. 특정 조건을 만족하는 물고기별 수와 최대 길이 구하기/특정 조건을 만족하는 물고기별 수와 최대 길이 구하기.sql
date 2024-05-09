with tmp as(
    select FISH_TYPE, ifnull(length, 10) as length 
    from FISH_INFO
)

select count(*) as FISH_COUNT, max(length) as MAX_LENGTH, fish_type 
from tmp
group by fish_type
having avg(length) > 33
order by fish_type

