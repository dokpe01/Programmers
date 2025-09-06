def solution(a, d, included):
    answer = 0
    num_lst = [a+d*i for i in range(len(included))]
    for i, j in zip(included, num_lst):
        if i:
            answer += j
    return answer