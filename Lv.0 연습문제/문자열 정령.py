def solution(my_string):
    answer = ''.join(sorted(list(my_string.lower())))
    return answer

a = "dEdfa"
print(solution(a))
'''
sort()는 반환하지 않는다.
반환을 이용하려면 sorted'''