select distinct c.CAR_ID, c.CAR_TYPE, round(30 * (c.daily_fee * ((100 - p.discount_rate) / 100))) as FEE
from car_rental_company_car as c join 
    car_rental_company_rental_history as h
    on c.car_id = h.car_id join
    car_rental_company_discount_plan as p
    on c.car_type = p.car_type and p.duration_type = '30일 이상'
where c.car_type in ('세단', 'SUV') 
    and c.CAR_ID NOT IN (
        SELECT CAR_ID
        FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
        WHERE START_DATE < '2022-12-01' AND END_DATE > '2022-11-01' 
    )
    
        
    and ((30 * (c.daily_fee * ((100 - p.discount_rate) / 100))) >= 500000 and 
    (30 * (c.daily_fee * ((100 - p.discount_rate) / 100))) < 2000000)
order by 3 desc, 2 asc, 1 desc