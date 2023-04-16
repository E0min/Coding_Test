def solution(spell, dic):
    answer = 2
    for i in dic:
        if len(i)==len(spell):
            count = 0
            for word in spell:
                if word in i:
                    count +=1
                if count == len(spell):
                    answer = 1
                    break
    return answer
