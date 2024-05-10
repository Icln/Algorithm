with cnt as(
    SELECT USER_ID
    from USER_INFO
    where year(JOINED) = 2021
)


select year(SALES_DATE) as year, month(SALES_DATE) as month, count(distinct(USER_ID)) as PUCHASED_USERS, 
ROUND(COUNT(distinct(USER_ID)) / (SELECT COUNT(USER_ID) FROM cnt),1) AS PUCHASED_RATIO
from ONLINE_SALE o
WHERE o.USER_ID IN (SELECT * FROM cnt)
GROUP BY year(SALES_DATE), month(SALES_DATE)
ORDER BY 1, 2
