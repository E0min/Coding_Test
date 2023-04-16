def solution(arr, divisor):
    answer = []
    answer = list(filter(lambda x:x%divisor==0,arr))
    if answer == []:
        answer.append(-1)
    return sorted(answer)