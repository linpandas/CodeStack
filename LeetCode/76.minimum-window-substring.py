#
# @lc app=leetcode.cn id=76 lang=python3
# @lcpr version=30204
#
# [76] 最小覆盖子串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        ans_left, ans_right = -1, len(s)
        left = 0
        counts = Counter()
        countt = Counter(t)
        for right, c in enumerate(s):
            counts[c] += 1
            while counts >= countt:
                if right - left < ans_right - ans_left:
                    ans_left, ans_right = left, right
                counts[s[left]] -= 1
                left += 1
        return "" if ans_left < 0 else s[ans_left: ans_right + 1]
        
# @lc code=end



#
# @lcpr case=start
# "ADOBECODEBANC"\n"ABC"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"a"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"aa"\n
# @lcpr case=end

#

