'''quiz = ["3 - 4 = -3","1 + 2 = 3"]
print(type(quiz[0]))
print(quiz[0].split(" "))
a=quiz[0].split(" ")
print(int(a[4]))
print(type(int(a[4])))
a = quiz[0]
print(type(eval(a[0:5])))
'''
def solution(quiz):
    answer = []
    
    for i in quiz: 
        a = i.split(" ") #문자열을 공백으로 스플릿하여 리스트로 저장
        
        if eval(i[0:5]) == int(a[4]):
            answer.append("O")
        else:
            answer.append("X")
            
    return answer

quiz = ["3 - 4 = -3","1 + 2 = 3","1 * 5 = 4","5 * 7 = 35"]
print(solution(quiz))
