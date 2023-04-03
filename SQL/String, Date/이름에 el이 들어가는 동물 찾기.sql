-- https://school.programmers.co.kr/learn/courses/30/lessons/59047
-- 코드를 입력하세요
SELECT animal_id, name
FROM animal_ins
where name like '%el%' and animal_type = 'dog'
order by name;