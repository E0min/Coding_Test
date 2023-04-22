def solution(n, arr1, arr2):
    answer =[]
    for a,b in zip(arr1,arr2):
        answer.append(sumbinary(binary(a,n),binary(b,n)))
            
    return answer

    
def binary(number,n):
    answer =[]
    while True:
        answer.append(number%2)
        number = number//2
        if number//2 == 0:
            answer.append(number%2)
            for i in range(n-len(answer)):
                answer.append(0)
            break
    return answer[::-1]

def sumbinary(list1,list2):
    re = ''
    for a,b in zip(list1, list2):
        if a+b==0:
            re += ' '
        elif a+b==1:
            re += '#'
        elif a+b==2:
            re += '#'
    return re
            