while True:
    length = int(input(''))
    if 1 <= length <= 100:
        break
    print('다시 입력하시오')

nums = input().strip()

total = 0
for ch in nums:
    total += int(ch)

print(total)

'''
length = int(input(''))

while True:
    if 1 <= length <= 100:
        break
    else:
        print('다시 입력해주십시오')

total = 0
for i in range(1, length + 1):
    num = int(input())
    total += num

print(total)
'''