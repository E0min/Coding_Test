-- https://school.programmers.co.kr/learn/courses/30/lessons/132203
-- 코드를 입력하세요
SELECT DR_NAME	,DR_ID	,MCDP_CD,date_format(HIRE_YMD,'%Y-%m-%d') HIRE_YMD
FROM DOCTOR
WHERE MCDP_CD = 'CS' or MCDP_CD = 'GS'
ORDER BY HIRE_YMD desc, DR_NAME	