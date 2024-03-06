#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            while left <= right and nums[left] != val:
                left += 1
            while right >= left and nums[right] == val:
                right -= 1
            if left < right:
                nums[left] = nums[right]
                right -= 1
        return right + 1
# @lc code=end

