# @lcpr-before-debug-begin
from python3problem209 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=209 lang=python3
# @lcpr version=30204
#
# [209] 长度最小的子数组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        minL = len(nums)
        curSum = 0
        if sum(nums) < target:
            return 0
        for r in range(len(nums)):
            curSum += nums[r]
            if curSum >= target:
                while curSum - nums[l] >= target:
                    curSum -= nums[l]
                    l += 1
                minL = min(minL, r-l+1)
        return minL
# @lc code=end



#
# @lcpr case=start
# 7\n[2,3,1,2,4,3]\n
# @lcpr case=end

# @lcpr case=start
# 4\n[1,4,4]\n
# @lcpr case=end

# @lcpr case=start
# 11\n[1,1,1,1,1,1,1,1]\n
# @lcpr case=end

#

