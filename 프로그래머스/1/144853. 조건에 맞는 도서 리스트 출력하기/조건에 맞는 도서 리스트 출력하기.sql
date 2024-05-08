SELECT BOOK_ID, to_char(published_date, 'yyyy-mm-dd') as PUBLISHED_DATE
FROM BOOK
WHERE CATEGORY = '인문' AND to_char(published_date, 'yyyy') = 2021
ORDER BY PUBLISHED_DATE;