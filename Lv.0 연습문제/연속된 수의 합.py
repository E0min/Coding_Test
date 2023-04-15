import math

def solution(num, total):
    answer = []
    if(num%2==0):
        low = math.floor(total/num)
        high = math.ceil(total/num)
        answer.append(low)
        answer.append(high)
        for i in range(1,(num-2)//2+1):
            answer.append(low-i)
            answer.append(high+i)
    else:
        middle = total//num
        answer.append(middle)
        for i in range(1,(num-1)//2 +1):
            answer.append(middle+i)
            answer.append(middle-i)
    answer.sort()        
    return answer
print(solution(5,15))