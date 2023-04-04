-- https://school.programmers.co.kr/learn/courses/30/lessons/131120
SELECT member_id, member_name, gender, DATE_FORMAT(date_of_birth,'%Y-%m-%d') DATE_OF_BIRTH
FROM member_profile
where date_of_birth like "%-03-%" and 
TLNO is not null and
gender = 'w'
order by member_id;