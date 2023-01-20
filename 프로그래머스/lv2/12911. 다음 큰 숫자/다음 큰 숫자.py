def solution(n):
    # 입력한 변수를 이진수로 변환했을 때 포함되는 1의 개수를 변수에 저장함 
    num1 = bin(n).count('1') 

    while True:
        n = n + 1
        if num1 == bin(n).count('1'):
            break
    return n