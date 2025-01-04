#
# @lc app=leetcode.cn id=17 lang=python3
# @lcpr version=30204
#
# [17] 电话号码的字母组合
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.letterMap = [
            "", # 0
            "", # 1
            "abc", # 2
            "def", # 3
            "ghi", # 4
            "jkl", # 5
            "mno", # 6
            "pqrs", # 7
            "tuv", # 8
            "wxyz" # 9
        ]
        result = []
        if not digits:
            return result
        self.backtracking(digits, 0, [], result)
        return result
    
    def backtracking(self, digits, index, path, result):
        if len(path) == len(digits):
            result.append("".join(path))
            return

        digit = int(digits[index])
        letters = self.letterMap[digit]
        for letter in letters:
            path.append(letter)
            self.backtracking(digits, index+1, path, result)
            path.pop()

# @lc code=end



#
# @lcpr case=start
# "23"\n
# @lcpr case=end

# @lcpr case=start
# ""\n
# @lcpr case=end

# @lcpr case=start
# "2"\n
# @lcpr case=end

#

