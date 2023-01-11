def solution(sides):
    answer = 0
    max_length = max(sides)
    sides.remove(max_length)
    other_length = sum(sides)
    if other_length>max_length:
        answer = 1
    else:
        answer = 2
    return answer
    '''
    배열에서 최대 최소값 찾기 -> max(배열), min(배열)
    리스트의 모든 원소 더하기 -> sum(리스트)
    리스트에서 요소 제거
    1. remove는 값을 제거
    2. pop은 인덱스로 제거, 
    3. del은 인덱스로 제거, 슬라이싱을 활용하여 제거 가능'''