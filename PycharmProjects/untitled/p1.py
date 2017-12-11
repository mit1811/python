def check_str(string):
    stack = []
    table = {
        ")": "(",
        "}": "{",
        "]": "[",
    }
    for char in string:
        if not stack:
            stack.append(char)
        elif char not in table:
            stack.append(char)
        elif table[char] == stack[-1]:
            stack.pop()
        else:
            stack.append(char)
    if stack:
        print("NO")
    else:
        print("YES")    

N = int(input().strip())
for i in range(N):
    check_str(input())