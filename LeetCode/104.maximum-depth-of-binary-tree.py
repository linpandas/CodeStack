#
# @lc app=leetcode.cn id=104 lang=python3
# @lcpr version=30204
#
# [104] 二叉树的最大深度
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         # 层序遍历
#         if not root:
#             return 0
#         from collections import deque
#         queue = deque([root])
#         result = 0
#         while queue:
#             result += 1
#             for _ in range(len(queue)):
#                 node = queue.popleft()
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
        
#         return result

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 后序遍历
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left, right) + 1
# @lc code=end



#
# @lcpr case=start
# [3,9,20,null,null,15,7]\n
# @lcpr case=end

# @lcpr case=start
# [1,null,2]\n
# @lcpr case=end

#

