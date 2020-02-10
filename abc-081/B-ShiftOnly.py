N = int(input())
A = list(map(int, input().split()))

ope_count = 0
while True:
    even_count = len([a for a in A if a % 2 == 0])

    if even_count != N:
        print(ope_count)
        break

    A = [a / 2 for a in A]
    ope_count += 1
