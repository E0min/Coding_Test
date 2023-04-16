-- https://school.programmers.co.kr/learn/courses/30/lessons/133025\
-- 코드를 입력하세요
SELECT ICECREAM_INFO.FLAVOR
FROM ICECREAM_INFO, FIRST_HALF 
WHERE TOTAL_ORDER > 3000 and INGREDIENT_TYPE = 'fruit_based' and ICECREAM_INFO.FLAVOR =  FIRST_HALF.FLAVOR