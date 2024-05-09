SELECT count(user_id) as users
FROM user_info
WHERE year(joined) = '2021' AND age >= 20 AND age <= 29;
