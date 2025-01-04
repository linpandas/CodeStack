#
# @lc app=leetcode.cn id=45 lang=python3
# @lcpr version=30204
#
# [45] 跳跃游戏 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        result = 0
        curd, nextd = 0, 0
        for i in range(len(nums)-1):
            nextd = max(nextd, i+nums[i])
            if i == curd:
                curd = nextd
                result += 1
        
        return result
# @lc code=end



#
# @lcpr case=start
# [2,3,1,1,4]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,0,1,4]\n
# @lcpr case=end

#

