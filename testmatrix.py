import numpy as np

rowNum = 7
colNum = 7
mat = np.zeros([rowNum,colNum])
for i in range(rowNum):
    for j in range(colNum):
        mat[i,j] = i - j
print(mat)
