#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        print(target)
        nums = sorted(nums)
        lenth = len(nums)
        # print(nums)
        dis = float("inf")
        res = 0
        for i in range(lenth):
            j = i+1
            k = lenth-1
            while j<k:
                s = nums[i]+nums[j]+nums[k]
                if s==target:
                    return s
                if abs(s-target)<dis:
                    dis = abs(s-target)
                    res = s
                if s-target>0:
                    k = k-1
                elif s-target<0:
                    j = j+1

            
        return res


# @lc code=end
s = Solution()
r = s.threeSumClosest([-1,2,1,-4],1)
print(r)