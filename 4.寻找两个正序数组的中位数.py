#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        element = list()
        lenn = len(nums1) + len(nums2)
        if lenn == 0:
            return 0
        i = 0
        j = 0
        while i < len(nums1) or j < len(nums2):
            if i == len(nums1):
                while j < len(nums2):
                    element.append(nums2[j])
                    j += 1
                break
            if j == len(nums2):
                while i < len(nums1):
                    element.append(nums1[i])
                    i += 1
                break
            if nums1[i] < nums2[j]:
                element.append(nums1[i])
                i += 1
            else:
                element.append(nums2[j])
                j += 1
        if lenn % 2 == 1:
            return element[lenn // 2]
        else:
            return (element[lenn // 2 - 1] + element[lenn // 2]) / 2
            
# @lc code=end
# list1 = [1, 2]
# list2 = [3, 4]
# s = Solution()
# result = s.findMedianSortedArrays(list1, list2)
# print(result)