def solution(my_string):
    answer = 0

    for i in range(len(my_string)):
        num=''
        if my_string[i].isdigit():
            num = num +my_string[i]
            while True:
                if my_string[i+1].isdigit():
                    num=num+my_string[i]
                    i = i+1
                else:
                    answer = answer + int(num)
                    break
                    
    return answer


    print(solution("123asdfsa4"))