def solution(wallet, bill):
    answer = 0
    while max(wallet) < max(bill) or min(wallet) < min(bill):
        bill[bill.index(max(bill))] = max(bill) // 2
        answer += 1
    return answer