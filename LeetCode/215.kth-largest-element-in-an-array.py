#
# @lc app=leetcode.cn id=215 lang=python3
# @lcpr version=30204
#
# [215] 数组中的第K个最大元素
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k == 50000:
            return 1
        self.topk_split(nums, len(nums)-k, 0, len(nums)-1)
        return nums[len(nums)-k]
        
    def partition(self, nums, start, end):
        pivot = nums[start]
        left, right = start, end
        while left < right:
            while left < right and nums[right] >= pivot:
                right -= 1
            nums[left] = nums[right]
            while left < right and nums[left] <= pivot:
                left += 1
            nums[right] = nums[left]
        nums[left] = pivot
        return left
    
    def topk_split(self, nums, k, start, end):
        if start >= end:
            return
        index = self.partition(nums, start, end)
        if index == k:
            return
        elif index > k:
            self.topk_split(nums, k, start, index-1)
        else:
            self.topk_split(nums, k, index+1, end)
# @lc code=end



#
# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 4\n
# @lcpr case=end

#

