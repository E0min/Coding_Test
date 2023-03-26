def solution(x):
    answer = 0
    
    return x%sum(int(i) for i in str(x))==0