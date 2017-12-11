def pangram(s):
    a="abcdefghijklmnopqrstuvwxyz"
    for i in a:
        if i not in s:
            return False
    return True
print pangram("qwertyuioplkjhgfdsazxcvbnmnhn")



