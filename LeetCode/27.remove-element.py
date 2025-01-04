#
# @lc app=leetcode.cn id=27 lang=python3
# @lcpr version=30204
#
# [27] 移除元素
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        for r in range(len(nums)):
            if nums[r] != val:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        
        return l
# @lc code=end



#
# @lcpr case=start
# [3,2,2,3]\n3\n
# @lcpr case=end

# @lcpr case=start
# [0,1,2,2,3,0,4,2]\n2\n
# @lcpr case=end

#

