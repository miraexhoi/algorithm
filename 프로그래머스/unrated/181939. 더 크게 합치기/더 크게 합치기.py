def solution(a, b):
    answer1 = str(a)+str(b)
    answer2 = str(b)+str(a)
    return int(answer1) if int(answer1) > int(answer2) else int(answer2)