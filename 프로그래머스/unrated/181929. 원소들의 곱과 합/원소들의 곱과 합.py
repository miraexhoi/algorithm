def solution(num_list):
    answer = 0
    summ1 = 1
    summ2 = 0
    
    for i in num_list:
        summ1 *= i
        summ2 += i
        
    answer = 1 if summ1 < summ2*summ2 else 0
    
    return answer