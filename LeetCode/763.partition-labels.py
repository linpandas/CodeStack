#
# @lc app=leetcode.cn id=763 lang=python3
# @lcpr version=30204
#
# [763] 划分字母区间
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurence = {}
        for i, c in enumerate(s):
            last_occurence[c] = i
        result = []
        start, end = 0, 0
        for i, c in enumerate(s):
            end = max(end, last_occurence[c])
            if i == end:
                result.append(end-start+1)
                start = end + 1
        
        return result
# @lc code=end



#
# @lcpr case=start
# "ababcbacadefegdehijhklij"\n
# @lcpr case=end

# @lcpr case=start
# "eccbbbbdec"\n
# @lcpr case=end

#

