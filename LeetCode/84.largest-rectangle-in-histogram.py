#
# @lc app=leetcode.cn id=84 lang=python3
# @lcpr version=30204
#
# [84] 柱状图中最大的矩形
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.insert(0, 0)
        heights.append(0)
        stack = []
        result = 0
        for r, height in enumerate(heights):
            while stack and heights[stack[-1]] > height:
                mid = stack.pop()
                if stack:
                    l = stack[-1]
                    w = r - l - 1
                    h = heights[mid]
                    result = max(result, w*h)
            stack.append(r)
        
        return result
# @lc code=end



#
# @lcpr case=start
# [2,1,5,6,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [2,4]\n
# @lcpr case=end

#

