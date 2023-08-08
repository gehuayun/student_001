print("每天要五分之一，需多少天可以超过一半")
a = 1
b = 0
c = 0

while True:
    c = c + a * 0.2
    b += 1
    if c >= 0.5:
        break
    a = a * 0.8
print(f"需要{b}天才能超过一半，一共有{c}")
