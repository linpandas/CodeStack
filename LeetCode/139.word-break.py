#
# @lc app=leetcode.cn id=139 lang=python3
# @lcpr version=30204
#
# [139] 单词拆分
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordSet = set(wordDict)
        dp = [False] * (n+1) # # dp[i]表示字符串的前i个字符是否可以被拆分成单词
        dp[0] = True
        for j in range(1, n+1): # 排列问题，先遍历背包
            for i in range(j): # 遍历单词
                if dp[i] and s[i:j] in wordSet:
                    dp[j] = True
        
        return dp[-1]
# @lc code=end



#
# @lcpr case=start
# "leetcode"\n["leet", "code"]\n
# @lcpr case=end

# @lcpr case=start
# "applepenapple"\n["apple", "pen"]\n
# @lcpr case=end

# @lcpr case=start
# "catsandog"\n["cats", "dog", "sand", "and", "cat"]\n
# @lcpr case=end

#

