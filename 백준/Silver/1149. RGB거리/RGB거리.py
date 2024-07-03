import sys
input = sys.stdin.readline

N = int(input())
colors = [list(map(int, input().split())) for i in range(N)]

memo = [[] for _ in range(N)]
memo[0] = colors[0]

for i in range(1,N):
    memo[i] = [
        colors[i][0] + min(memo[i-1][1],memo[i-1][2]),
        colors[i][1] + min(memo[i-1][0],memo[i-1][2]),
        colors[i][2] + min(memo[i-1][0],memo[i-1][1]),
    ]

print(min(memo[N-1]))
