num = int(input())
way = int(input())

result = ""

if num == 0:
    result = "0"
else:
    while num > 0:
        remainder = num % way
        num = num // way

        if remainder >= 10:
            result = chr(ord('A') + remainder - 10) + result
        else:
            result = str(remainder) + result

print(result)
