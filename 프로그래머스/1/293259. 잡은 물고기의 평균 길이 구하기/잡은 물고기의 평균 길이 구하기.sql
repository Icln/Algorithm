with tmp as(
    select ifnull(LENGTH, 10) as length
    from FISH_INFO
)

select round(avg(length), 2) as AVERAGE_LENGTH
from tmp