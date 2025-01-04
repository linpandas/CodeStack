#
# @lc app=leetcode.cn id=226 lang=python3
# @lcpr version=30204
#
# [226] 翻转二叉树
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
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 前序遍历（递归法）
        if not root:
            return root
        
        root.left, root.right = root.right, root.left
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        return root
# class Solution:
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         # 前序遍历（迭代法）
#         if not root:
#             return root
#         stack = [root]
#         while stack:
#             node = stack.pop()
#             node.left, node.right = node.right, node.left
#             if node.right:
#                 stack.append(node.right)
#             if node.left:
#                 stack.append(node.left)
        
#         return root

# class Solution:
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         # 层序遍历
#         if not root:
#             return root
#         from collections import deque
#         queue = deque([root])
#         while queue:
#             node = queue.popleft()
#             node.left, node.right = node.right, node.left
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
        
#         return root

# class Solution:
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         # 后序遍历（递归法）
#         if not root:
#             return root
        
#         left = self.invertTree(root.left)
#         right = self.invertTree(root.right)
#         root.left, root.right = root.right, root.left

#         return root
# class Solution:
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         # 后序遍历（迭代法）
#         if not root:
#             return root
#         stack = [root]
#         while stack:
#             node = stack.pop()
#             if node.left:
#                 stack.append(node.left)
#             if node.right:
#                 stack.append(node.right)
#             node.left, node.right = node.right, node.left
        
#         return root

# class Solution:
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         # 中序遍历(递归法)
#         if not root:
#             return root
        
#         left = self.invertTree(root.left)
#         root.left, root.right = root.right, root.left
#         right = self.invertTree(root.left)

#         return root
# class Solution:
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         # 中序遍历（迭代法）
#         if not root:
#             return root
        
#         stack = [root]
#         while stack:
#             node = stack.pop()
#             if node.left:
#                 stack.append(node.left)
#             node.left, node.right = node.right, node.left
#             if node.left:
#                 stack.append(node.left)
        
#         return root
# @lc code=end



#
# @lcpr case=start
# [4,2,7,1,3,6,9]\n
# @lcpr case=end

# @lcpr case=start
# [2,1,3]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#

