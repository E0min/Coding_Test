
def solution(chicken):
    wchicken=chicken+1
    while chicken//10 > 0:
        wchicken += chicken%10
        chicken = chicken//10
    print(wchicken)
    service=0
    while wchicken//10>0:
        service += wchicken//10
        wchicken = wchicken//10
    answer = service
    return answer

print(solution(1081))