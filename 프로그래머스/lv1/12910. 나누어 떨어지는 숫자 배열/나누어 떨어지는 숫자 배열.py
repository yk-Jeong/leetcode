def solution(arr, divisor):
    answer = []
    
    for i in range(len(arr)):
        if (arr[i] % divisor) == 0: # 나머지가 0이 아니면
            answer.append(arr[i]) # 원소를 삭제
        else:
            pass
    
    if len(answer) > 0:
        answer = sorted(answer)
    else:
        answer.append(-1)
        
    return answer