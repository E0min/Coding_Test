def solution(s, n):
    answer = ''
    for a in s:
        if a.isupper(): # A~Z 65~90
            answer += chr((ord(a)+n-65)%26+65)
        elif a.islower(): # a~z
            answer += chr((ord(a)+n-97)%26+97)
        else:
            answer += ' '
    return answer