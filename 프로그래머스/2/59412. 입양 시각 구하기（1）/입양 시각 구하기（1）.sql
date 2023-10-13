select date_format(datetime, '%H') as HOUR, count(*) as COUNT
from animal_outs
where date_format(datetime, '%H:%i') between '09:00' and '19:59'
group by HOUR
order by HOUR