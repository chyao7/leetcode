#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start
class Solution:
    def exist(self, board, word: str) -> bool:
        def dfs(i,j,k):
            # print(board,k,i,j)
            if k==len(word):
                return True
            
            if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or board[i][j]!=word[k] :
                return False
            board[i][j]=''
            res = dfs(i+1,j,k+1) or dfs(i-1,j,k+1) or dfs(i,j+1,k+1) or dfs(i,j-1,k+1)
            board[i][j]=word[k]
            return res
        
        if len(board)*len(board[0])<len(word):
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,0):
                    return True
        return False
        
# @lc code=end

if __name__=="__main__":
    S = Solution()
    l =S.exist([["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]],"AAAAAAAAAAAAAAB")
    print(l)