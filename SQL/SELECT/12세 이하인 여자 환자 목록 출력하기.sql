-- https://school.programmers.co.kr/learn/courses/30/lessons/132201
-- 코드를 입력하세요
SELECT PT_NAME,PT_NO,GEND_CD,AGE,ifnull(TLNO,'NONE')
FROM PATIENT
WHERE AGE <= 12 and GEND_CD = 'W'
ORDER BY AGE desc, PT_NAME