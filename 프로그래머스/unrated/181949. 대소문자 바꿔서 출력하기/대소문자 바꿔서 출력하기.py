a = input()
result = ""
for i in a:
    if 97<=ord(i)<=122:
        result += i.upper()
    else:
        result += i.lower()
    
print(result)