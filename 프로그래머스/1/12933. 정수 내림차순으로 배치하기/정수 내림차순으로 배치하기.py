def solution(n):
    answer = []
    
    for i in str(n):
        answer.append(int(i))
        
    answer.sort(reverse=True)
    answer = int(''.join(map(str, answer)))
    return answer