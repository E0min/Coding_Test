import math
def solution(n):
    answer = 0
    while True:
        k=1
        if n>math.factorial(k):
            k = k + 1
        else:
            answer = k
            break
    return answer

print(solution(3))