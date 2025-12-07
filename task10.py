while True:
    num = int(input())
    if 1 <= num <= 1000:
        break
    print("다시 입력하시오")

while True:
    times = list(map(int, input().split()))

    # 길이 맞는지 체크
    if len(times) != num:
        print("다시 입력하시오")
        continue

    # 범위 체크
    if all(1 <= t <= 1000 for t in times):
        break

    print("다시 입력하시오")

times.sort()
total = 0
acc = 0

for t in times:
    acc += t
    total += acc

print(total)
