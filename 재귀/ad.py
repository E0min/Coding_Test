arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

row = arr[0]  # 첫 번째 행 추출
column = [row[1] for row in arr]  # 두 번째 열 추출

submatrix = [row[1:3] for row in arr]  # 각 행에서 두 번째와 세 번째 열 추출

print(submatrix)