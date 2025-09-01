def solution(n):
    answer = 0
    while True:
        answer += 6
        if answer % n == 0:
            return int(answer/6)