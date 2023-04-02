-- 코드를 입력하세요
SELECT name,count(name) countname
from animal_ins
group by name having countname>=2
order by name;