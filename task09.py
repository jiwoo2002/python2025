num = int(input())

# 대각선 번호 찾기
line = 1
while line * (line + 1) // 2 < num:
    line += 1

# 대각선 내 위치
which = num - (line - 1) * line // 2

# 분수 계산
if line % 2 == 1:
    a = line - which + 1
    b = which
else:
    a = which
    b = line - which + 1

print(f"{a}/{b}")
