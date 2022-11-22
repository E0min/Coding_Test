def solution(babbling):
    answer = 0
    for i in babbling:
        i =i.replace('aya','0')
        i =i.replace('ye','0')
        i =i.replace('woo','0')        
        i =i.replace('ma','0')
        print(i)

        if (i == '0') or (i == '00') or (i == '000') or (i == '0000'):
            answer = answer + 1
            print(f'옹알이{answer}')

        
    return answer
solution(	["ayaye", "woo", "ye", "yemawoo", "ayaa"])