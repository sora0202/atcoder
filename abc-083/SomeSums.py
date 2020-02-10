input = input().split()
N = int(input[0])
A = int(input[1])
B = int(input[2])

ans = 0

for i in range(1, N + 1):
    digits = list(map(int, str(i)))
    s = sum(digits)

    if A <= s and s <= B:
        ans += i

print(ans)
