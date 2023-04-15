'''
def solution(s):
    answer = ''
    li = s.split(' ')
    for i in li:
        index = 0
        while index<len(i):
            i[index].upper if index%2==1 else i[index].lower()
            index+=1
            
    answer = ' '.join(li)
    return answer'''

li = ['sadf','sgfg','jknk']

for i in li:
        index = 0
        while index < len(i):
            if index%2==1:
                 i[index] = i[index].lower() 
            else:
                  i[index] = i[index].upper()
            index+=1
print(li)
            
