def solution(sizes):
    answer = 0
    for i in sizes:
        i.sort()
    answer = max([i[0] for i in sizes])*max(i[1]for i in sizes)
    return answer