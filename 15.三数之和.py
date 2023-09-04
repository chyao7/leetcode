#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        # print(nums)
        lenth = len(nums)
        res = []
        for i in range(lenth):
            j = i+1
            k = lenth-1
            while j<k:
                if nums[j]+nums[k]==-nums[i]:
                    # print(i,j,k,nums[i],nums[j],nums[k])
                    if [nums[i],nums[j],nums[k]] not in res:
                        res.append([nums[i],nums[j],nums[k]])
                    j= j+1
                if nums[j]+nums[k]>-nums[i]:
                    k = k-1
                if nums[j]+nums[k]<-nums[i]:
                    j = j+1
        return res
    
# @lc code=end
s=Solution()
s.threeSum([-1,0,1,2,-1,-4])