#
# @lc app=leetcode.cn id=79 lang=python3
# @lcpr version=30204
#
# [79] 单词搜索
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        def dfs(i, j, k) -> bool:
            if not 0 <= i < m or not 0 <= j < n or board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            board[i][j] = ""
            result = dfs(i+1, j, k+1) or dfs(i-1, j, k+1) or \
                dfs(i, j+1, k+1) or dfs(i, j-1, k+1)
            board[i][j] = word[k]
            return result
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False
        
# @lc code=end



#
# @lcpr case=start
# [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"\n
# @lcpr case=end

# @lcpr case=start
# [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"SEE"\n
# @lcpr case=end

# @lcpr case=start
# [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCB"\n
# @lcpr case=end

#

