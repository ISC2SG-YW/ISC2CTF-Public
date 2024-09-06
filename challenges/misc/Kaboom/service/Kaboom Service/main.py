import random 
import time
import os
def generateGrid(n):
    grid = [[random.randint(-9999,99999) for i in range(n)] for j in range(n)]
    grid[0][0] = 0
    return grid

def findPath(grid,E):
    
    n = len(grid)
    E = min(E + 1 ,2*(n-1)+1) # Since we are starting from 0, and maximum energy that can be used to reach the end is 2n -1 (i put 2n to be safe)
    dp = [[[0 if j == 0 and k == 0 else -float('inf') for i in range(E+1)] for j in range(n+1)] for k in range(n+1)]
    
    for i in range(1,n+1):
        for j in range(1,n+1):
            for k in range(1,E+1):
                dp[i][j][k] = max(dp[i-1][j][k-1],dp[i][j-1][k-1],dp[i-1][j-1][k-1])+grid[i-1][j-1]
    return max(dp[n][n])

def main():
    testCases = [5,25,50,75,100,150,175,200,200,200]
    for testNo,testCase in enumerate(testCases):
        grid = generateGrid(testCase)
        if random.choice([True,False]):
            energy = random.randint(testCase-1,testCase*2)
        else:
            energy = random.randint(testCase*2,1e9)
        print(f"Test Case {testNo+1}")
        print(testCase)
        print(energy)
        for row in grid:
            print(" ".join(map(str,row)))
        maximumEnergy = findPath(grid,energy)
        curTime = time.time()
        guessedEnergy = input("")
        timeTaken = time.time() - curTime
        if timeTaken > 60:
            print("Time Limit Exceeded :c")
            return
        if int(guessedEnergy) == maximumEnergy:
            print("Correct!")
        else:
            print("Incorrect!")
            return 
    print(f"All test cases passed! Heres the flag: {os.getenv('FLAG')}")
    
if __name__ == "__main__":
    main()