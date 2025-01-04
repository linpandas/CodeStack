#
# @lc app=leetcode.cn id=105 lang=python3
# @lcpr version=30204
#
# [105] 从前序与中序遍历序列构造二叉树
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root_val = preorder[0]
        root = TreeNode(root_val)

        seperate_idx = inorder.index(root_val)

        inorder_left = inorder[:seperate_idx]
        inorder_right = inorder[seperate_idx+1:]

        preorder_left = preorder[1:len(inorder_left)+1]
        preorder_right = preorder[len(inorder_left)+1:]

        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)

        return root
        
# @lc code=end



#
# @lcpr case=start
# [3,9,20,15,7]\n[9,3,15,20,7]\n
# @lcpr case=end

# @lcpr case=start
# [-1]\n[-1]\n
# @lcpr case=end

#

