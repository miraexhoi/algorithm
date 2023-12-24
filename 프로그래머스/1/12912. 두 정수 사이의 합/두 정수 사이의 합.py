def solution(a, b):
    answer = 0
    if a < b:
        for i in range(a, b+1):
            answer += i
        return answer
    elif a == b:
        return a
    elif a > b:
        for i in range(a, b-1, -1):
            answer += i
        return answer