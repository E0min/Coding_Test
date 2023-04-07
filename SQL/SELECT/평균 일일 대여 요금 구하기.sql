-- https://school.programmers.co.kr/learn/courses/30/lessons/151136
-- 코드를 입력하세요
SELECT round(avg(DAILY_FEE),0) AVERAGE_FEE
FROM CAR_RENTAL_COMPANY_CAR
WHERE CAR_TYPE = 'SUV';