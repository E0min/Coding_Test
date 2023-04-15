-- https://school.programmers.co.kr/learn/courses/30/lessons/144853
-- 코드를 입력하세요
SELECT BOOK_ID, DATE_FORMAT(PUBLISHED_DATE,'%Y-%m-%d')
FROM BOOK
WHERE (PUBLISHED_DATE between '2021-01-01' and '2021-12-31') and CATEGORY = '인문'
ORDER BY PUBLISHED_DATE;