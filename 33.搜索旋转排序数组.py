#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if target in nums:
            k = nums.index(target)
            return k
        else:
            return -1


# @lc code=end

