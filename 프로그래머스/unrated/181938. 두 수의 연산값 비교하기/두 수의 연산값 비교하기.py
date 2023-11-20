def solution(a, b):
    first = str(a)+str(b)
    second = 2*a*b
    if int(first) >= second:
        return int(first)
    else:
        return second