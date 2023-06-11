def solution(A,B):
    
    A.sort()
    B.sort(reverse=True)
    
    answer = A[0] * B[0]
    
    for i in range(1, len(A)):
        answer = answer + A[i] * B[i]
            
    return answer