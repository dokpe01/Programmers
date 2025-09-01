def solution(str_list, ex):
    answer = ''
    for i in str_list:
        answer += i if ex not in i else ''
    return answer