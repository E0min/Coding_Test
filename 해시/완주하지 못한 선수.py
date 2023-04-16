from collections import Counter
def solution(participant, completion):
    partdict = Counter(participant)
    comdict = Counter(completion)
    answer = ''.join(list((partdict-comdict).keys()))
        
    
    return answer