def solution(a, b):
    if a%b==0:
        return 1
    else:
        m = set(div(b//gcd(a,b)))
    
    if m == {1} or m=={2} or m=={5} or m=={2,5} or m=={5,2}:
        return 1
    else:
        return 2
    

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
    
def div(num):
    count = 2
    li=[]
    while True:
        if num%count==0:
            li.append(count)
            num = num // count
        else:
            count+=1
        if num//1 ==1:
            return li
            break
            
            