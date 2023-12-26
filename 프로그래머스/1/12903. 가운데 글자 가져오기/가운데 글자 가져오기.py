def solution(s):
    a = len(s)//2
    if len(s) % 2 == 0:
        answer = s[a-1] + s[a]
        return answer
    else:
        answer = s[a]
        return answer