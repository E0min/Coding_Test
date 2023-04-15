def solution(my_string):
    answer = 0
    i = 0
    while i < len(my_string)-2:
        num=''
        while my_string[i].isdigit():
            num += my_string[i]
            i = i + 1
            if not my_string[i+1].isdigit():
                answer = answer + int(num)
        i = i + 1
    return answer
print(solution('123asd1s2f'))