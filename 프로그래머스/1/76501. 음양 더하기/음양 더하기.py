def solution(absolutes, signs):
    answer = 0
    
    for x in range(len(absolutes)):
        if not signs[x]:
            answer -= int(absolutes[x])
        else:
            answer += int(absolutes[x])
            
    return answer