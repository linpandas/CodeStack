#
# @lc app=leetcode.cn id=1143 lang=python3
# @lcpr version=30204
#
# [1143] 最长公共子序列
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 动态规划
        m, n = len(text1), len(text2)
        # 长度为i-1的字符串text1与长度为j-1的字符串text2
        # 最长公共子序列为dp[i][j]
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[-1][-1]
# @lc code=end



#
# @lcpr case=start
# "abcde"\n"ace"\n
# @lcpr case=end

# @lcpr case=start
# "abc"\n"abc"\n
# @lcpr case=end

# @lcpr case=start
# "abc"\n"def"\n
# @lcpr case=end

#

