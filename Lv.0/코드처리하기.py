def solution(code):
    answer = ''
    mode = 0
    for i, value in enumerate(code):
        if value == "1":
            mode += 1
            continue
        if mode % 2 == 0:
            if i % 2 == 0:
                answer += value
        else:
            if i % 2 != 0:
                answer += value
    return "EMPTY" if answer == '' else answer