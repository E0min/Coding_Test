def solution(number, limit, power):
    answer=0
    for i in range(1,number+1):
        a = div(i)
        answer = answer +power if a>limit else answer +a 
    return answer

def div(number):
    ans=0
    for i in range(1, int(number**(1/2))+1):
        if i**2==number:
            ans +=1
        elif number % i == 0:
            ans +=2
        
    return ans



'''def solution(number, limit, power):
    
    if ((number>=1)&(number<=100000))&((limit>=2)&(limit<=100))&((power>=1)&(power<=limit)):
        answer = 0
        for a in range(1,number+1): # 1~number의 기사단원을 도는 반복문
            divisor = 0
            for k in range(1,int(a**(1/2))+1): 
                if (a**(1/2))%1==0: # 제곱근이 정수인경우
                    if a % k  == 0:
                        divisor =+ 1 
                    divisor = divisor*2-1
                else:
                    if a % k  == 0:
                        divisor =+ 1 
                    divisor = divisor * 2 
            

            if divisor > limit:
                answer = answer + power
            else:
                answer = answer + divisor
            print(answer)
        return answer


solution(10,3,2)
'''
'''
def solution(number, limit, power):
    answer = 0
    for a in range(1,number+1): # 1~number의 기사단원을 도는 반복문
        divisor = 0
        if (a % 2 == 0)&(a>1): # 짝수 기사단원
            divisor =+ 1
            for k in range(1,a//2+1): # 
                if a % k  == 0:
                    divisor = divisor + 1 
        else: # 홀수 기사단원
            for k in range(1,a+1): #각 기사단원의 약수갯수구하는 반복문
                if a % k  == 0:
                    divisor = divisor + 1 

        if divisor > limit:
            answer = answer + power
            print(answer)
        else:
            answer = answer + divisor
            print(answer)
    return answer
'''