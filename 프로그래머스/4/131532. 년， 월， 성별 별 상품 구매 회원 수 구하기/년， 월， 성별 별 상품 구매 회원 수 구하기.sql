select  date_format(o.sales_date, '%Y') as YEAR,
        date_format(o.sales_date, '%m') as MONTH,
        u.gender as GENDER, 
        count(distinct u.user_id) as USERS
from user_info as u
    join online_sale as o
    on u.user_id = o.user_id and u.gender is not NULL
group by YEAR, MONTH, GENDER
order by 1, 2, 3