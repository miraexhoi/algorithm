def solution(n):
    answer = ''
    a = n//2
    answer = "수박"*a
    
    if n % 2 == 0:
        return answer
    else:
        return answer + "수"