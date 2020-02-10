N = int(input())
A = list(map(int, input().split()))

is_alice_turn = True

alice_point = 0
bob_point = 0

while len(A) != 0:
    picked_num = max(A)
    if is_alice_turn:
        alice_point += picked_num
    else:
        bob_point += picked_num

    A.remove(picked_num)
    is_alice_turn = not is_alice_turn

print(alice_point - bob_point)
