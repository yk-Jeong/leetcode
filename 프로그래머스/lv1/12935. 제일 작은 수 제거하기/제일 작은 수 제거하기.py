def solution(answer):
    
    answer.remove(min(answer))
    
    if len(answer) == 0:
        answer.append(-1)
    else:
        pass
    
    return answer