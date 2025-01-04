#
# @lc app=leetcode.cn id=394 lang=python3
# @lcpr version=30204
#
# [394] 字符串解码
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res, multi = "", 0
        for c in s:
            if c == "[":
                stack.append((res, multi))
                res, multi = "", 0
            elif c == "]":
                cur_res, cur_multi = stack.pop()
                res = cur_res + res*cur_multi
            elif "0" <= c <= "9":
                multi = multi * 10 + int(c)
            else:
                res += c
        
        return res
# @lc code=end



#
# @lcpr case=start
# "3[a]2[bc]"\n
# @lcpr case=end

# @lcpr case=start
# "3[a2[c]]"\n
# @lcpr case=end

# @lcpr case=start
# "2[abc]3[cd]ef"\n
# @lcpr case=end

# @lcpr case=start
# "abc3[cd]xyz"\n
# @lcpr case=end

#

