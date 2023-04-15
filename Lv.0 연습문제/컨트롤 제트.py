def solution(s):
    answer = 0
    S = s.split()
    for i in range(len(S)):
        if S[i].isdecimal():
            answer += int(S[i])
        elif S[i]=='Z':
            answer -= int(S[i-1])
        else:
            answer += int(S[i])
    return answer


s = "-1 -2 Z"
print(solution(s))