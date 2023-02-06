def solution(s):
    answer = True    
    
    # s의 대소문자를 대문자로 통일
    s = s.upper()
    
    # 둘 다 0이 아니면서 
    if (s.count('P') == 0) and (s.count('Y') == 0):
        answer = True
    else:
        if s.count('P') != s.count('Y'): # 같지 않을 경우 
            answer = False
        elif s.count('P') == s.count('Y'): # 같을 경우 
            answer = True
    
    return answer