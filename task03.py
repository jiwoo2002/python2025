price = int(input('금액 입력: '))
money = 1000
change = money - price
count = 0

fhun = change // 500
change %= 500

hun = change // 100
change %= 100

fifty = change // 50
change %= 50

ten = change // 10
change %= 10

five = change // 5
one = change % 5

count = fhun + hun + fifty + ten + five + one
print(f"동전 개수 합계: {count}")
