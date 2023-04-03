-- https://school.programmers.co.kr/learn/courses/30/lessons/131535
SELECT  count(user_id) users
FROM USER_INFO
WHERE (AGE BETWEEN 20 AND 29) and 
(joined between '2021-01-01' and '2021-12-31');