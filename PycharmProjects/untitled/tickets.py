arr=[ 5, 2, 6, 3 ,4 ,5 ]
pos=3
def calculate_time(arr, pos):
    i = 0
    time = -1
    while arr[pos] !=0:
        if arr[i] == 0:
            pos-=1
            continue
        if(i == len(arr)):
            i = 0
            time+=1
        arr[i] = arr[i] - 1
        i+=1
    return time

def main():
    time = calculate_time(arr, pos)
    print time
main()