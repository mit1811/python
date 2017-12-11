number=int(input())
def prime_num(number):
    if(number>1):
        for i in range(2,number):
            if(number%i==0):
                break
        else:
            return number
print prime_num(23)
