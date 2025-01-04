#
# @lc app=leetcode.cn id=739 lang=python3
# @lcpr version=30204
#
# [739] 每日温度
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i, item in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < item:
                result[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        
        return result
# @lc code=end



#
# @lcpr case=start
# [73,74,75,71,69,72,76,73]\n
# @lcpr case=end

# @lcpr case=start
# [30,40,50,60]\n
# @lcpr case=end

# @lcpr case=start
# [30,60,90]\n
# @lcpr case=end

#

