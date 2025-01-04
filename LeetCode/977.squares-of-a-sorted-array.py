#
# @lc app=leetcode.cn id=977 lang=python3
# @lcpr version=30204
#
# [977] 有序数组的平方
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        result = []
        while l <= r:
            if nums[l] + nums[r] > 0:
                result.append(nums[r] ** 2)
                r -= 1
            else:
                result.append(nums[l] ** 2)
                l += 1
        
        return result[::-1]
# @lc code=end



#
# @lcpr case=start
# [-4,-1,0,3,10]\n
# @lcpr case=end

# @lcpr case=start
# [-7,-3,2,3,11]\n
# @lcpr case=end

#

