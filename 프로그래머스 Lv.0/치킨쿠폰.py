
def solution(chicken):
    chicken_service = 0
    while True:
        chicken_service = chicken_service + chicken//10
        coupon = chicken//10 + chicken%10
        chicken = coupon
        
    return chicken_service

print(solution(1081))