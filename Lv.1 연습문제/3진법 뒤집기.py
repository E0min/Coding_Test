def solution(n):
    answer = 0
    tri = []
    while n//3 != 0:
        tri.append(n%3)
        n = n//3
        if n//3 ==0:
            tri.append(n)
    trilen=len(tri)-1
    print(trilen)
    print(tri)
    for i in tri:
        answer = answer + i*(3**trilen)
        trilen -=1
        
        
    
    return answer


print(solution(1))