s = input().split()
N = int(s[0])
Y = int(s[1])

for a in range(N + 1):
    for b in range(N - a + 1):
        c = N - a - b
        if a * 10000 + b * 5000 + c * 1000 == Y:
            print(str(a) + " " + str(b) + " " + str(c))
            exit(0)

print("-1 -1 -1")
