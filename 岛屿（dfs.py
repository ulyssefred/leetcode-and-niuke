class Solution:
    def dfssolution(self,i,j):
        dx = [1,0,-1,0]
        dy = [0,-1,0,1]
        for k in range(4):
            if 0<=i+ dx[k]<self.m and 0<=j+ dy[k]<self.n and self.grid[i+dx[k]][j+dy[k]]== 1:
                self.grid[i+dx[k]][j+dy[k]] = 0
                self.dfssolution(i+dx[k], j+dy[k])
    def solve(self , grid ):
        if grid == [] or grid == [[]]:
            return 0
        self.grid = grid
        self.m,self.n = len(grid),len(grid[0])
        res = 0
        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == 1:
                    res +=1
                    self.grid[i][j] =0
                    self.dfssolution(i, j)
        return res
test = Solution()
testlist = [[1,1,0,0,0],[0,1,0,1,1],[0,0,0,1,1],[0,0,0,0,0],[0,0,1,1,1]]
testlist1 =[[1]]
print(test.solve(testlist1))