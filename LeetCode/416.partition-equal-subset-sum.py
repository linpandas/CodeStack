#
# @lc app=leetcode.cn id=416 lang=python3
# @lcpr version=30204
#
# [416] 分割等和子集
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_ = sum(nums)
        if sum_ % 2 == 1:
            return False
        target = sum_ // 2
        dp = [0] * (target+1) # # 容量为j的背包，所背的物品价值最大可以为dp[j]
        for num in nums:
            for j in range(target, num-1, -1):
                dp[j] = max(dp[j], dp[j-num]+num)
        if dp[target] == target:
            return True
        return False
# @lc code=end



#
# @lcpr case=start
# [1,5,11,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,5]\n
# @lcpr case=end

#

