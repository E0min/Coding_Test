-- 코드를 입력하세요
SELECT warehouse_id, warehouse_name, address, ifnull(freezer_yn,'N') 
from food_warehouse 
where address like '%경기도%' 
order by warehouse_id;

-- ifnull(조사하려는 칼럼,NULL값 일시 출력되는 것)