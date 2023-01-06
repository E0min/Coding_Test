def solution(my_string):
    answer = ''

    for i in range(len(my_string)):
        num=''
        if my_string[i].isdigit():
            num +=my_string[i]
            for a in range(i+1,len(my_string)):
                if my_string[a].isdigit():
                    num +=my_string[a]
                else:
                    break
        answer = answer + num
    return answer

print(solution("a234ffg"))