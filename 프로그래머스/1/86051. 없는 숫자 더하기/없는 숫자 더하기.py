def solution(numbers):
    answer = 0
    new = [0,1,2,3,4,5,6,7,8,9]
    
    for i in range(len(numbers)):
        if numbers[i] in new:
            new.remove(numbers[i])

    for i in new:
        answer += i
        
    return answer