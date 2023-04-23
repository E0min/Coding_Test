def solution(a, b, n):# 콜라 a병을 주면 b병을 준다.
    answer = 0
    recent=n
    if n<a:
        return answer
    else:
        return (recent // a)*b + solution(a,b,recent%a + (recent // a)*b) # 현재 병 = 남은 병 + 받은 병
        
print(solution(2,	1,	20))