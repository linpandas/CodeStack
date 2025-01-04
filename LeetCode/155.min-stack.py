#
# @lc app=leetcode.cn id=155 lang=python3
# @lcpr version=30204
#
# [155] 最小栈
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class MinStack:
    ## 栈中元素为(当前的值val，栈内最小值)
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            self.stack.append((val, min(self.stack[-1][1], val)))

    def pop(self) -> None:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end



#
# @lcpr case=start
# ["MinStack","push","push","push","getMin","pop","top","getMin"][[],[-2],[0],[-3],[],[],[],[]]\n
# @lcpr case=end

#

