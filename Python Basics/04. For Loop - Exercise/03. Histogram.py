n = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for number in range(n):
    now = int(input())
    if now < 200:
        p1 += 1
    elif 200 <= now < 400:
        p2 += 1
    elif 400 <= now < 600:
        p3 += 1
    elif 600 <= now < 800:
        p4 += 1
    else:
        p5 += 1

for i in [p1, p2, p3, p4, p5]:
    print(f"{i / n * 100:.2f}%")
