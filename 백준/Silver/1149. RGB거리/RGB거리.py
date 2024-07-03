import sys
input = sys.stdin.readline

N = int(input())
colors = [list(map(int, input().split())) for i in range(N)]

memo = [[] for _ in range(N)]
memo[0] = colors[0]

for i in range(1,N): # n+1 번째 집은 n번째 집이 어떤 색깔을 칠했는지에 대한 정보가 필요함.
    memo[i] = [      # n 번째 집의 RGB 경우의 수에서 n-1번째 의 최솟값을 더해주고 이를 배열에 저장하는 bottom-up dp방식을 활용
        colors[i][0] + min(memo[i-1][1],memo[i-1][2]),
        colors[i][1] + min(memo[i-1][0],memo[i-1][2]),
        colors[i][2] + min(memo[i-1][0],memo[i-1][1]),
    ]

print(min(memo[N-1]))
