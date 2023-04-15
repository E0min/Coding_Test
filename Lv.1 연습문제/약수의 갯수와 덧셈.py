def solution(left, right):
    answer = 0
    for a in range(left,right+1):
        div = 0
        for b in range(1,a+1):
            if a%b==0:
                div+=1
        if div%2==0:
            answer +=a
        else:
            answer -=a
    return answer