def solution(my_string, overwrite_string, s):
    before = my_string[:s]
    btw = my_string[s:len(overwrite_string)+s]
    after = my_string[len(overwrite_string)+s:]
    return before + overwrite_string + after