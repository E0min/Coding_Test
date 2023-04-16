def solution(common):
    if((common[0]+common[2])/2 == common[1]):
        answer =  (common[1]-common[0]) + common.pop() 
    else:
         answer = (common[1]//common[0]) *common.pop() 
    return answer


list = [2,4,8]
print(solution(list))