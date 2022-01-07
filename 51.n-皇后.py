#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int):
        self.a = [0]*n
        self.res = []
        # print(self.dfs(n,0))
        self.res.append(self.dfs(n,0))
        print(self.res)
        return 

    def dfs(self,n,row):
        if row == n:
            return self.a[:]
        for i in range(n):
            if self.check(row, i):
                self.a[row] = i
                # print (self.a, i, self.a[i])
                self.dfs(n,row+1)
                self.a[row] = 0

    def check(self,row ,e):
        for i in range(row):
            if self.a[i]==e: return False
            if (self.a[i]+i)==(row+e):return False
            if (self.a[i]-i) == (e-row): return False
        return True




        

# @lc code=end

if __name__=="__main__":
    s = Solution()
    s.solveNQueens(n=4)