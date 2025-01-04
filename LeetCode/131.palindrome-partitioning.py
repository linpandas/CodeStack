#
# @lc app=leetcode.cn id=131 lang=python3
# @lcpr version=30204
#
# [131] 分割回文串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        self.backtracking(s, 0, [], result)
        return result
        
    def backtracking(self, s, startIndex, path, result):
        if startIndex == len(s):
            result.append(path.copy())
            return
        for i in range(startIndex, len(s)):
            if s[startIndex:i+1] == s[startIndex:i+1][::-1]:
                path.append(s[startIndex:i+1])
                self.backtracking(s, i+1, path, result)
                path.pop()
# @lc code=end



#
# @lcpr case=start
# "aab"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n
# @lcpr case=end

#

