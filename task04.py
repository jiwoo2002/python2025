num = input('숫자 입력: ')
if len(num) == 1:
    num = "0" + num

original = num
count = 0

while True:
    a = int(num[0])
    b = int(num[1])
    result = (a + b) % 10
    num = num[1] + str(result)
    count += 1
    if num == original:
        break

print(count)
