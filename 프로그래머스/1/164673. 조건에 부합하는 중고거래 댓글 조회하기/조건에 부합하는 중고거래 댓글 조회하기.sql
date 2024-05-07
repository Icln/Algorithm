SELECT b.TITLE, b.BOARD_ID, r.REPLY_ID, r.WRITER_ID, r.CONTENTS, to_char(r.CREATED_DATE, 'yyyy-mm-dd') created_date
from USED_GOODS_BOARD b, USED_GOODS_REPLY r
where b.BOARD_ID = r.BOARD_ID
and b.CREATED_DATE
between to_date('2022-10-01', 'yyyy-mm-dd') and to_date('2022-10-31', 'yyyy-mm-dd')
order by r.CREATED_DATE asc, b.TITLE asc