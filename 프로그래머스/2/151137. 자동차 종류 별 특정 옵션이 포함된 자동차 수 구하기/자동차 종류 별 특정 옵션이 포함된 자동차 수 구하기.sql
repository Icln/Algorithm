select CAR_TYPE, count(*) as CARS
from car_rental_company_car
where options REGEXP '통풍시트|열선시트|가죽시트'
group by car_type
order by car_type