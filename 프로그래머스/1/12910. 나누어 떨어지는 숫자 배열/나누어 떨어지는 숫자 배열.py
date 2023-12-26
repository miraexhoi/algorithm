def solution(arr, divisor):
    new = []
    
    for i in arr:
        if i % divisor == 0:
            new.append(i)
    
    if len(new) != 0:
        new.sort()
        return new
    else:
        return [-1]