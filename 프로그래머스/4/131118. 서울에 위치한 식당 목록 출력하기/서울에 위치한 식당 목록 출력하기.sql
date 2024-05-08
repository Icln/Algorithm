select i.REST_ID, i.REST_NAME, i.FOOD_TYPE, i.FAVORITES, i.ADDRESS, round(avg(r.review_score), 2) as score
from REST_INFO i join REST_REVIEW r on i.REST_ID = r.REST_ID
where i.address like '서울%'
group by i.rest_id,i.REST_NAME, i.FOOD_TYPE, i.FAVORITES, i.ADDRESS
order by score desc, i.FAVORITES desc