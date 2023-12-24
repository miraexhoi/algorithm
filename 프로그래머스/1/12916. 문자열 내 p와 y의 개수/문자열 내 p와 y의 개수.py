def solution(s):
    cntI = 0
    cntY = 0
    for i in s:
        if (i == "p") or (i == "P"):
            cntI += 1
        if (i == "y") or (i == "Y"):
            cntY += 1
    if cntI == cntY:
        return True
    else:
        return False