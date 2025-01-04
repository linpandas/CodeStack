#
# @lc app=leetcode.cn id=152 lang=python3
# @lcpr version=30204
#
# [152] 乘积最大子数组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        premin, premax = nums[0], nums[0]
        for num in nums[1:]:
            curmin = min(premin*num, premax*num, num)
            curmax = max(premin*num, premax*num, num)
            result = max(result, curmax)
            premin, premax = curmin, curmax
        
        return result
# @lc code=end



#
# @lcpr case=start
# [2,3,-2,4]\n
# @lcpr case=end

# @lcpr case=start
# [-2,0,-1]\n
# @lcpr case=end

#

