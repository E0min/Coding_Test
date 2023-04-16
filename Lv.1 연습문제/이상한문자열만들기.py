def solution(s):
    
    li = list(s)
    index = 0
    for i in range(len(li)):
        if li[i]== ' ':
            index=0
        elif index%2==0:
            li[i]=li[i].upper()
            index +=1
        else:
            li[i]=li[i].lower()
            index +=1
        
    return ''.join(li)