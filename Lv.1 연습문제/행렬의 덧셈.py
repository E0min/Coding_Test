def solution(arr1, arr2):
    answer = []
    for a,b in zip(arr1,arr2):
        answer.append([x+y for x,y in zip(a,b)])
                
    return answer

def solution(arr1, arr2):
    return [[x+y for x,y in zip(a,b)] for a,b in zip(arr1,arr2)]
                
