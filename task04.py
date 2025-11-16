num = int(input())

original = num
count = 0

while True:
    a = num // 10
    b = num % 10
    result = (a + b) % 10
    num = b * 10 + result
    count += 1
    if num == original:
        break

print(count)
