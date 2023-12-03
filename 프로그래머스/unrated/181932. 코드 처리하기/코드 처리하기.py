def solution(code):
    result = ""
    mode = 0
    
    for i in range(len(code)):
        if mode == 0 : 
            if code[i] != '1' and i % 2 == 0:
                result += code[i]
            elif code[i] == '1':
                mode = 1
        else :
            if code[i] != '1' and i % 2 == 1 :
                result += code[i]
            elif code[i] == '1':
                mode = 0
    if result == '':
        return 'EMPTY'
    return result
