def solution(my_string, alp):
    alp_upper = alp.upper()
    if alp in my_string:
        answer = my_string.replace(alp, alp_upper)
        return answer
    else:
        return my_string