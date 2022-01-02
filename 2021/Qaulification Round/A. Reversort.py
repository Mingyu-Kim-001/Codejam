import sys


def calculations(L):
    ans = 0
    for i in range(len(L) - 1):
        j = min(range(i, len(L)), key=lambda x: L[x])
        L = L[:i] + L[i : j + 1][::-1] + L[j + 1:]
        ans += j - i + 1
    return ans
    
T = int(sys.stdin.readline().rstrip())
for t in range(T):
    N = int(sys.stdin.readline().rstrip())
    L = [int(num) for num in sys.stdin.readline().rstrip().split(" ")]
    print(f'Case #{t + 1}: {calculations(L)}')