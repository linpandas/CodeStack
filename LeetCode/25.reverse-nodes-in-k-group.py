#
# @lc app=leetcode.cn id=25 lang=python3
# @lcpr version=30204
#
# [25] K 个一组翻转链表
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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur, n = head, 0
        while cur:
            n += 1
            cur = cur.next
        p0 = dummy = ListNode(next=head)
        while n >= k:
            n -= k
            cur, pre = p0.next, None
            for i in range(k):
                temp = cur.next
                cur.next = pre
                pre = cur
                cur = temp
            nxt = p0.next
            p0.next.next = cur
            p0.next = pre
            p0 = nxt
        
        return dummy.next
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n3\n
# @lcpr case=end

#

