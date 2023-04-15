def solution(n):
    answer = 0
    str = "{}".format(n)
    
    for i in str:
        answer  = answer+int(i)
        
    return answer
    '''
    숫자 자료형을 문자열로 바꾸는 방법
    1. str()
    2. "{}".format()
    '''