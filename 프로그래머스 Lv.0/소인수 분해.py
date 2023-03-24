def solution(n):
    answer = []
    number = n
        
    for i in range(2,n+1): # 2~n까지
        while number%i==0:
            number = number//i
            answer.append(i)
    return sorted(list(set(answer)))
                
        