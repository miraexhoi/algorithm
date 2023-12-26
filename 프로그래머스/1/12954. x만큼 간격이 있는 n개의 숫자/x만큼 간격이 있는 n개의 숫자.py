def solution(x, n):
    answer = []
    xx = x
    
    for i in range(n):
        answer.append(xx)
        xx += x
        
    return answer