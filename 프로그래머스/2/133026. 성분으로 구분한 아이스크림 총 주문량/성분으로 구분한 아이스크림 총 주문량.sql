SELECT i.INGREDIENT_TYPE, sum(total_order) as TOTAL_ORDER
FROM FIRST_HALF as f
    INNER JOIN ICECREAM_INFO as i ON f.flavor = i.flavor  
GROUP BY i.ingredient_type