N = int(input())
D = [int(input()) for i in range(N)]

cnt = 0
pre_diameter = 101

while len(D) != 0:
    diameter = max(D)
    if diameter < pre_diameter:
        cnt += 1

    D.remove(diameter)
    pre_diameter = diameter

print(cnt)
