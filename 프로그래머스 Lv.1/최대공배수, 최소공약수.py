def solution(n, m):
    answer = []
    return answer


def max(x): #x를 구성하는 서로소의 집합
    quo=x
    se={}
    while quo != 1:
        for i in range(2,x+1):
            if quo // i == 0:
                se.add(i)
                quo = quo // i

    return se

print(max(6))
