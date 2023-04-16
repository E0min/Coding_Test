def solution(n):
    i=0
    a=0
    while a<n:
        i = i + 1 
        a += 1
        while i%3==0 or ( '3' in str(i) ) :
            i = i + 1
        print(i)
    return i


print(solution(100))