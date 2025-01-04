#
# @lc app=leetcode.cn id=300 lang=python3
# @lcpr version=30204
#
# [300] 最长递增子序列
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n # dp[i]表示i之前的包括i的以nums[i]为结尾的最长递增序列的长度
        for j in range(n):
            for i in range(j+1):
                if nums[j] > nums[i]:
                    # 注意这里不是要dp[j] 与 dp[i] + 1进行比较，
                    # 而是我们要取dp[i] + 1的最大值。
                    dp[j] = max(dp[j], dp[i]+1)
        
        return max(dp)
# @lc code=end



#
# @lcpr case=start
# [10,9,2,5,3,7,101,18]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,0,3,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [7,7,7,7,7,7,7]\n
# @lcpr case=end

#

