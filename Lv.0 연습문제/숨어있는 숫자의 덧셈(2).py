def solution(my_string):
    answer = 0
    ans =''
    for i in range(len(my_string)):
        if my_string[i].isdigit():
            ans += my_string[i]
        else:
            if ans != '' or my_string[len(my_string)-1].isdigit():
                print(ans)
                answer += int(ans)
            ans = ''
        i =+ 1
    return answer

print(solution('123asd1s2f2'))