def bin(number,n):
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


print(bin(7,5))