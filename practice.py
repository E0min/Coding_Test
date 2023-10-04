<<<<<<< Updated upstream
from itertools import combinations
def solution(numbers):
    return sorted(list(set([sum(x) for x in combinations(numbers,2)])))
=======
def div(number):
    ans=0
    for i in range(1, int(number**(1/2))+1):
        if i**2==number:
            ans +=1
        elif number % i == 0:
            ans +=2
        
    return ans


print(div(25))
print(div(16))
print(div(8))
>>>>>>> Stashed changes
