def solution(arr):
    sumn = 0
    for i in arr:
        sumn += i
    avg = sumn/len(arr)
    return avg