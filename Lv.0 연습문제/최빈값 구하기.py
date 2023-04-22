from collections import Counter
def solution(array):
    artdict=Counter(array)
    
    tmp = [k for k,v in artdict.items() if max(artdict.values())==v]
    if len(tmp) != 1:
        return -1
    else:
        return tmp[0]
    ##max(artdict,key=artdict.get)
    