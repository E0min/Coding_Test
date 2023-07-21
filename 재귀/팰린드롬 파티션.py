def palindrome(n): # n은 처음 팰린드롬을 구할 수 
    if n<=1:
        count[0] += 1
    else:
        for i in range(n//2):
            palindrome(i)
        

if __name__ =="__main__":
    count =[1]
    
    print(count[0])
