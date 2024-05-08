select DR_NAME, DR_ID, MCDP_CD, to_char(HIRE_YMD, 'yyyy-mm-dd')
from doctor
where MCDP_CD = 'CS' or MCDP_CD = 'GS' 
order by HIRE_YMD desc, DR_NAME
