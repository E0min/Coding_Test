
def solution(n):
    answer = 0
    for i in range(1, n//2+2):
        if i**2 == n:
            return (i+1)**2
    return -1



