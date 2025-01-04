#
# @lc app=leetcode.cn id=94 lang=python3
# @lcpr version=30204
#
# [94] 二叉树的中序遍历
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
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         # 递归法
#         if not root:
#             return []
#         left = self.inorderTraversal(root.left)
#         right = self.inorderTraversal(root.right)

#         return left + [root.val] + right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 迭代法
        if not root:
            return []
        stack = []
        result = []
        cur = root
        while cur or stack:
            # 左中右
            # 先访问最底层的左子树节点
            if cur:
                stack.append(cur)
                cur = cur.left
            # 到达最左节点后处理栈顶节点
            else:
                cur = stack.pop()
                result.append(cur.val)
                cur = cur.right
        return result
# @lc code=end



#
# @lcpr case=start
# [1,null,2,3]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

