#
# @lc app=leetcode.cn id=20 lang=python3
# @lcpr version=30204
#
# [20] 有效的括号
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {")":"(", "]":"[", "}":"{"}
        for c in s:
            if c in dic.values():
                stack.append(c)
            elif not stack or dic[c] != stack[-1]:
                return False
            else:
                stack.pop()
        
        return not stack
# @lc code=end



#
# @lcpr case=start
# "()"\n
# @lcpr case=end

# @lcpr case=start
# "()[]{}"\n
# @lcpr case=end

# @lcpr case=start
# "(]"\n
# @lcpr case=end

# @lcpr case=start
# "([])"\n
# @lcpr case=end

#

