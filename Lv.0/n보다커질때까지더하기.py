def solution(numbers, n):
    result = 0
    for i in numbers:
        if result > n:
            break
        else:
            result += i
    return result