--https://school.programmers.co.kr/learn/courses/30/lessons/164673
SELECT TITLE,used_goods_reply.BOARD_ID,REPLY_ID,used_goods_reply.WRITER_ID,used_goods_reply.CONTENTS,date_format(used_goods_reply.CREATED_DATE,'%Y-%m-%d')
FROM used_goods_reply,USED_GOODS_BOARD
where used_goods_reply.board_id=USED_GOODS_BOARD.board_id and
USED_GOODS_BOARD.created_date between '2022-10-01' and '2022-10-31'
order by used_goods_reply.created_date,USED_GOODS_BOARD.title;