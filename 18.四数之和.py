#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums = sorted(nums)
        length = len(nums)
        res = []
        for i in range(length-3):
            target2 = target - nums[i]
            for j in range(i+1,length-2):
                m = j+1
                n = length-1
                if nums[i]+nums[j]>target and nums[j]>0:
                    break
                while m<n:
                    if nums[m]+nums[n]+nums[j]==target2:
                        if [nums[i],nums[j],nums[m],nums[n]] not in res:
                            res.append([nums[i],nums[j],nums[m],nums[n]])
                        m +=1
                    if nums[m]+nums[n]+nums[j]>target2:
                        n = n-1
                    elif nums[m]+nums[n]+nums[j]<target2:
                        m = m+1
                    # print(m,n)
                    
        return res
# @lc code=end
S = Solution()
res =S.fourSum([1,-2,-5,-4,-3,3,3,5],-11)
print(res)