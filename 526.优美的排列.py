#
# @lc app=leetcode.cn id=526 lang=python3
#
# [526] 优美的排列
#

# @lc code=start






class Solution:
    def __init__(self) -> None:
        self.res = 0

    def countArrangement(self, n: int) -> int:

        def solve(index,li):
            if index-1==n:
                    # print(li,n,"xx")
                self.res +=1
            for i in range(n):
                
                # if i+1>len(li):
                    # continue
                if i+1 in li:
                    continue
                # print(li,i+1)
                if index%(i+1)==0 or (i+1)%index==0:
                    # print(li,i)
                # print(li,i)
                    li.append(i+1)
                    solve(index+1,li)
                    # return
                    li.pop()
        solve(1,[])
        # print(len(self.res))
        return self.res
# @lc code=end
n = 15
s = Solution()
s.countArrangement(n)