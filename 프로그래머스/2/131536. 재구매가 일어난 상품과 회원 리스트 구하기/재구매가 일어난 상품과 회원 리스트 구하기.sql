select user_id, product_id
from online_sale
group by user_id, product_id
having count(online_sale_id) >= 2
order by user_id, product_id desc