# A~Z : 65~90,a~z : 97~122
text = input()

result = ""

for ch in text:
    code = ord(ch)

    if 65 <= code <= 90:
        result += chr(code + 32)

    elif 97 <= code <= 122:
        result += chr(code - 32)

    else:
        result += ch

print(result)
