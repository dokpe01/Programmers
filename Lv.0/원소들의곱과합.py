def solution(num_list):
    answer1, answer2 = 0, 1
    for i in range(len(num_list)):
        answer2 *= num_list[i]
        answer1 += num_list[i]
    return 1 if answer1**2 > answer2 else 0