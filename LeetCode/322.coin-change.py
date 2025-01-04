#
# @lc app=leetcode.cn id=322 lang=python3
# @lcpr version=30204
#
# [322] 零钱兑换
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount+1) # 凑足总额为j所需的最小钱币数量为dp[j]
        dp[0] = 0
        for coin in coins:
            for j in range(coin, amount+1):
                dp[j] = min(dp[j], dp[j-coin]+1)
        if dp[amount] == float("inf"):
            return -1
        return dp[-1]
# @lc code=end



#
# @lcpr case=start
# [1, 2, 5]\n11\n
# @lcpr case=end

# @lcpr case=start
# [2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n0\n
# @lcpr case=end

#

