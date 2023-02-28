def solution(x, n):
    answer = []
    
    # 조건에 x=정수라고 되어 있으므로 
    # x != 0인 경우와 x = 0인 경우를 나누어 생각해야 함
    
    if x != 0:
        for i in range(x, x*(n+1), x):
            answer.append(i)
    else:
        for i in range(n):
            answer.append(0)
        
    return answer