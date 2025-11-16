while True:
    length = int(input(''))
    if 1 <= length <= 1000000:
        break
    print('다시 입력하시오')

numbers = []
for i in range(length):
    while True:
        num = int(input(''))
        if -1000000 <= num <= 1000000:
            numbers.append(num)
            break
        print('다시 입력하시오')

max_number = max(numbers)
min_number = min(numbers)

print(max_number, min_number)
