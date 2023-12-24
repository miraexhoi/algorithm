def solution(x):
    summ = 0
    
    for i in str(x):
        summ += int(i)
        
    if x % summ == 0:
        return True
    else:
        return False