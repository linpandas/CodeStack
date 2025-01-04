#
# @lc app=leetcode.cn id=2 lang=python3
# @lcpr version=30204
#
# [2] 两数相加
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode()
        remainder = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            total = x + y + remainder
            remainder = total // 10
            cur.next = ListNode(total % 10)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            cur = cur.next
        if remainder:
            cur.next = ListNode(remainder)
        return dummy.next
# @lc code=end



#
# @lcpr case=start
# [2,4,3]\n[5,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n[0]\n
# @lcpr case=end

# @lcpr case=start
# [9,9,9,9,9,9,9]\n[9,9,9,9]\n
# @lcpr case=end

#

