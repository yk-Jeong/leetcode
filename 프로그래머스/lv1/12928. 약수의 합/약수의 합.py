def solution(n):
    answer = []

    for i in range(1, n+1):        
        if (n % i) != 0: 
            pass
        else:
            answer.append(i)

    answer = sum(set(answer))
    
    return answer