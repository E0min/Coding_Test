def gcd(m,n): #m>n
    if m//n==0:
        return n
    else:
        gcd(n,m%n)
        

print(gcd(120,36))