import math
def solution(my_str, n):
    length = len(my_str)
    a = math.ceil(length/n)
    answer=[]
    for i in range(a):
        answer.append(my_str[0:n])
        my_str = my_str[n:]
    return answer