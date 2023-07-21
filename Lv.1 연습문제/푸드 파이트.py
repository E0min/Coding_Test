def solution(food):
    answer = ''
    foodd=[]
    for i in food:
        if i%2==0:
            foodd.append(i//2)
        else:
            foodd.append((i-1)//2)
            
    for a,b in zip(foodd[1:],range(1,len(foodd[1:]))):  
        # a는 foodd 의 갯수, b는 foodd의 인덱스
        for i in range(1,a+1):
            answer = answer + b
        print(answer)
        
    return answer

print(solution([12,23,53]))