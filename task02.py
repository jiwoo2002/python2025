import random

matrix = []

for i in range(9):
    row = []  # 각 행을 위한 리스트
    for j in range(9):
        n = random.randint(0, 99)
        row.append(n)
    matrix.append(row)

print(matrix)

max_num = 0
max_row = 0
max_col = 0


for i in range(9):
    for j in range(9):
        if matrix[i][j] > max_num:
            max_num = matrix[i][j]
            max_row = i
            max_col = j

print("최댓값:",max_num)
print("행:",max_row + 1," 열:",max_col + 1)
