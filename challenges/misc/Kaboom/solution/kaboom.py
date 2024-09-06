from pwn import * 

r = remote('127.0.0.1', 323)
def findPath(grid,E):
    
    n = len(grid)
    E = min(E + 1 ,2*(n-1)+1) # Since we are starting from 0, and maximum energy that can be used to reach the end is 2n -1 (i put 2n to be safe)
    dp = [[[0 if j == 0 and k == 0 else -float('inf') for i in range(E+1)] for j in range(n+1)] for k in range(n+1)]
    
    for i in range(1,n+1):
        for j in range(1,n+1):
            for k in range(1,E+1):
                dp[i][j][k] = max(dp[i-1][j][k-1],dp[i][j-1][k-1],dp[i-1][j-1][k-1])+grid[i-1][j-1]
    return max(dp[n][n])

def answer():
    print(r.recvline())
    n = int(r.recvline().strip().decode())
    e = int(r.recvline().strip().decode())
    grid = []
    for _ in range(n):
        grid.append(list(map(int,r.recvline().strip().decode().split(" "))))
    answerOf = findPath(grid,e)
    print(answerOf)
    r.sendline(str(answerOf))
    print(r.recvline())
    
    
for _ in range(10):
    answer()
print(r.recvall().decode())
        