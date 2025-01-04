#
# @lc app=leetcode.cn id=19 lang=python3
# @lcpr version=30204
#
# [19] 删除链表的倒数第 N 个结点
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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        pre, cur = dummy, dummy
        for i in range(n+1):
            cur = cur.next
        while cur:
            pre, cur = pre.next, cur.next
        pre.next = pre.next.next
        return dummy.next
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n1\n
# @lcpr case=end

#

