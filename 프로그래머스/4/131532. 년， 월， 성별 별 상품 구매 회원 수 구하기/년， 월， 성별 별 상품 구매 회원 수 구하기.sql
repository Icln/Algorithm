select year(sales_date) as year, month(sales_date) as month, gender, count(distinct o.user_id) as users
from USER_INFO u join ONLINE_SALE o on u.user_id = o.user_id
where gender is not null
group by year(sales_date), month(sales_date), gender
order by 1, 2, 3