import sys

def reverse(L, start_idx, end_idx):
    l, r = start_idx, end_idx
    while l <= r:
        L[l], L[r] = L[r], L[l]
        l, r = l + 1, r - 1

def restore(L, N, cost, start_idx):
    if start_idx < 0:
        return L
    current_cost = min(N - start_idx, cost - start_idx)
    reverse(L, start_idx, start_idx + current_cost - 1)
    return restore(L, N, cost - current_cost, start_idx - 1)


T = int(sys.stdin.readline().rstrip())
for t in range(T):
    N, cost = [int(num) for num in sys.stdin.readline().rstrip().split(" ")]
    print(f'Case #{t + 1}: ', end="")
    if not (N - 1 <= cost <= N * (N + 1) // 2 - 1):
        print("IMPOSSIBLE")
    else:
        print(" ".join([str(num) for num in restore(list(range(1,N + 1)), N, cost, N - 2)]))