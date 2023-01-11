a =123
def solution(num_list, n):
    answer = []
    for i in range(len(num_list)+1/n):
    answer.append(num_list[i*n:i*n+n])
    return answer