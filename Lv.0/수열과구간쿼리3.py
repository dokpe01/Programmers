def solution(arr, queries):
    for i in queries:
        q1, q2 = arr[i[0]], arr[i[1]]
        arr[i[0]] = q2
        arr[i[1]] = q1
    return arr