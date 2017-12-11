matrix = [[0, 1, 1, 2],
          [0, 5, 0, 0],
          [2, 0, 3, 3]]
matrix1=[row[0]for row in matrix]
matrix2=[row[1] for row in matrix]
matrix3=[row[2] for row in matrix]
matrix4=[row[3] for row in matrix]
print matrix1
print matrix2
print matrix3
print matrix4
for i in range (0,len(matrix1)-1):
    for j in range(1,len(matrix1)):
        if (matrix1[i]==0):
            del(matrix1[i+1])
print matrix1
for i in range(0,len(matrix2)-1):
    for j in range(1, len(matrix2)):
        if (matrix2[i]==0):
            del(matrix2[i+1])
print matrix2
for i in range(0,len(matrix3)-1):
    for j in range(1, len(matrix3)):
        if (matrix3[i]==0):
            del(matrix3[i+1])
print matrix3
for i in range(0,len(matrix4)-1):
    for j in range(1, len(matrix4)):
        if (matrix4[i]==0):
            del(matrix4[i+1])
print matrix4