
#n과 m 입력
while True:
    n = int(input("바구니의 갯수 입력: "))
    if 0 <= n <= 100:
        break
    else:
        print("0 이상 100 이하의 숫자만 입력하시오.")

while True:
    m = int(input("공을 바꿀 횟수 입력: "))
    if 0 <= m <= 100:
        break
    else:
        print("0 이상 100 이하의 숫자만 입력하시오.")

basket = []
for i in range(0, n):
    basket.append(i +1)

for i in range(m):
    print((i + 1),'번째 턴')
    while True:
        location1 = int(input('첫번째 위치: '))
        location2 = int(input('두번째 위치: '))
        if 0 <= location1 <= n:
            if 0 <= location2 <= n:
                break
            else:
                print('잘못된 입력입니다')

    tmp_number = 0
    tmp_number = basket[location1-1]
    basket[location1-1] = basket[location2-1]
    basket[location2-1] = tmp_number

print(basket)
