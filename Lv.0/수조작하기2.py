def solution(numLog):
    answer = ''
    dic = {1:"w", -1:"s", 10:"d", -10:"a"}
    for i in range(1,len(numLog)):
        v = numLog[i] - numLog[i-1]
        answer += dic[v]
            
    return answer