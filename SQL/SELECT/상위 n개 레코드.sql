--https://school.programmers.co.kr/learn/courses/30/lessons/59405
SELECT name from animal_ins 
where datetime = (
select min(datetime)
from animal_ins);