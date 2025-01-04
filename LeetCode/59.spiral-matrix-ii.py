#
# @lc app=leetcode.cn id=59 lang=python3
# @lcpr version=30204
#
# [59] 螺旋矩阵 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for _ in range(n)]
        l, r, t, b = 0, n-1, 0, n-1
        k = 1
        while True:
            for j in range(l, r+1):
                matrix[t][j] = k
                k += 1
            t += 1
            if t > b:
                break
            for i in range(t, b+1):
                matrix[i][r] = k
                k += 1
            r -= 1
            if l > r:
                break
            for j in range(r, l-1, -1):
                matrix[b][j] = k
                k += 1
            b -= 1
            if t > b:
                break
            for i in range(b, t-1, -1):
                matrix[i][l] = k
                k += 1
            l += 1
            if l > r:
                break
        
        return matrix
# @lc code=end



#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

