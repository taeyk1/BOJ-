import sys
input = sys.stdin.readline

n = int(input())
dp = [list(map(int, input().split())) for i in range(n)]
for i in range(n-1, 0, -1):
    temp = []
    for j in range(0, i):
        dp[i-1][j] = max([dp[i-1][j]+dp[i][j], dp[i-1][j]+dp[i][j+1]]) # bottom-up dp
print(max(dp[0]))
    
