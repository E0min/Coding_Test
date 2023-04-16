def solution(s):
    p = s.upper().count('P')
    y = s.upper().count('Y')
    if (p==0 and y ==0) or p==y:
        return True
    else:
        return False