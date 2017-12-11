matrix = [[0, 1, 1, 2],
          [0, 5, 0, 0],
          [2, 0, 3, 3]]
result=zip(*matrix)
sum=0
for i in result:
    for j in i:
        if j == 0:
            break
        sum+=j
print sum