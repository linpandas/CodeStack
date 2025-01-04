#
# @lc app=leetcode.cn id=70 lang=python3
# @lcpr version=30204
#
# [70] 爬楼梯
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1) # # 爬到第i个台阶，有dp[i]种方法
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[-1]
# @lc code=end



#
# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 3\n
# @lcpr case=end

#

