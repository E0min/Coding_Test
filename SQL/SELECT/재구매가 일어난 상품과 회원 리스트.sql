-- https://school.programmers.co.kr/learn/courses/30/lessons/131536
SELECT distinct USER_ID, PRODUCT_ID
FROM ONLINE_SALE
group by user_id,product_id
having  count(*)>=2 -- having은 group by 절에 대한 조건/ where은 전체 테이블에 대해 요구하는 조건
ORDER BY USER_ID asc, PRODUCT_ID desc;