import sys
def palindrome(n):
    if n<=1:
        count[0] += 1
        
    else:
        for i in range(n//2+1):
            if check[i] is not None:
                palindrome(i)
            else:
                count[0] = count[0] + check[i]


check = [] # 팰린드롬 파티션을 저장하는 배열
count =[0] # 횟수를 저장하는 배열
a = int(sys.stdin.readline())
b = [int(sys.stdin.readline()) for _ in range(a)]
for i in b:
    palindrome(i)
    print(count[0])
    count[0] = 0

