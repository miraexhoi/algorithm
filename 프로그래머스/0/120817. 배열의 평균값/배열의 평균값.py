def solution(numbers):
    hap = 0
    for i in numbers:
        hap += int(i)
        
    answer = hap / len(numbers)
    return answer