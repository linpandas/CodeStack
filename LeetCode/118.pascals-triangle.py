#
# @lc app=leetcode.cn id=118 lang=python3
# @lcpr version=30204
#
# [118] 杨辉三角
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # 动态规划
        dp = [[1]*i for i in range(1, numRows+1)]
        for i in range(2, numRows):
            for j in range(1, i):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        
        return dp
# @lc code=end



#
# @lcpr case=start
# 5\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

