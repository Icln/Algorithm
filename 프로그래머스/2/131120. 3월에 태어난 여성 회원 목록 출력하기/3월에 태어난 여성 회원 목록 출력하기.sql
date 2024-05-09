SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d') as DATE_OF_BIRTH
from MEMBER_PROFILE
WHERE month(DATE_OF_BIRTH) = 3
AND TLNO != 'NULL'
AND GENDER = 'W'
order by MEMBER_ID