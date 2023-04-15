def solution(dots):
    answer = 0
    x = set([dots[0][0],dots[1][0],dots[2][0],dots[3][0]])
    y = set([dots[0][1],dots[1][1],dots[2][1],dots[3][1]])
    x1 =list(x)
    y1 = list(y)
    dx = abs(x1[0]-x1[1])
    dy = abs(y1[0]-y1[1])
    answer = dx*dy
    return answer