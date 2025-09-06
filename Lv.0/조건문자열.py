def solution(ineq, eq, n, m):
    if eq == "!":
        return 1 if eval(str(n)+ineq+str(m)) else 0
    else:
        return 1 if eval(str(n)+ineq+'='+str(m)) else 0