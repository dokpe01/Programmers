def solution(l, r):
    result = []
    cnt = 0
    num = [1, 2, 3, 4, 6, 7, 8, 9]
    for i in range(l, r+1):
        if len(str(i)) > 1:
            for j in range(len(str(i))):
                if int(str(i)[j:j+1]) in num:
                    cnt = 0
                    break
                else:
                    cnt += 1
            if cnt == len(str(i)):
                result.append(i)
        else:
            if int(str(i)) not in num:
                result.append(i)
    if result == []:
        result.append(-1)
    return result