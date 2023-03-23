def solution(keyinput, board):
    answer = [0, 0]
    board_sero = (board[1] - 1) // 2
    board_garo = (board[0] - 1) // 2
    for i in keyinput:
        if i == "right" and board_garo>answer[0]:
            answer[0] = answer[0] + 1
        elif i == "left" and -board_garo<answer[0]:
            answer[0] = answer[0] - 1
        elif i == "up" and board_sero>answer[1]:
            answer[1] = answer[1] + 1
        elif i == "down" and -board_sero<answer[1]:
            answer[1] = answer[1] - 1
            
    return answer