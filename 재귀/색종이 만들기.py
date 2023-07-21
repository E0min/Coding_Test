# 백준 재귀 2630번
from typing import Sequence,Any

def recur(li):
    n = len(li[0])//2 # n의 길이를 구한다.
    if 2*n == 1:
        count[check(li)] += 1
        return
    else:
        for a in range(0,n+1,n):# a는 0,n 반복
            for b in range(0,n+1,n): # b는 0,n 반복
                submat = [i[b:b+n] for i in li[a:a+n]]

                if check(submat)==0:
                    count[check(submat)]+=1

                elif check(submat)==1:
                    count[check(submat)]+=1

                elif check(submat)==2:
                    recur(submat)

    
def check(li:Sequence):
    add=0
    for i in li: #입력받은 종이가 무슨 색인지 알아내서 리턴
        add = add + sum(i)
    if add == 0:
        return 0 # 흰종이
    if add == len(li)*len(li):
        return 1 # 검은 종이
    else:
        return 2
    


if __name__ == '__main__':
    n = int(input(":"))
    sakjonge=[list(map(int, input().split())) for _ in range(n)]
    count=[0,0] # 0은 흰종이, 1은 검은 종이
    recur(sakjonge)
    
    print(count[0])
    print(count[1])