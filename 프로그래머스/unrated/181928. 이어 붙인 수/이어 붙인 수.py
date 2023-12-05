def solution(num_list):
    odd = ''
    even = ''
    answer = ''
    
    for i in num_list:
        if i % 2 != 0:
            odd += str(i)  
        else:
            even += str(i)
    
    answer = int(odd) + int(even)
    return answer