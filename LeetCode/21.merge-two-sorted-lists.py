#
# @lc app=leetcode.cn id=21 lang=python3
# @lcpr version=30204
#
# [21] 合并两个有序链表
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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 迭代法
        dummy = node = ListNode()
        while list1 and list2:
            if list1.val > list2.val:
                node.next = list2
                list2 = list2.next
            else:
                node.next = list1
                list1 = list1.next
            node = node.next
        node.next = list1 if list1 else list2
        return dummy.next

# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         # 递归法
#         if not list1:
#             return list2
#         if not list2:
#             return list1
#         if list1.val > list2.val:
#             list2.next = self.mergeTwoLists(list1, list2.next)
#             return list2
#         else:
#             list1.next = self.mergeTwoLists(list1.next, list2)
#             return list1
# @lc code=end



#
# @lcpr case=start
# [1,2,4]\n[1,3,4]\n
# @lcpr case=end

# @lcpr case=start
# []\n[]\n
# @lcpr case=end

# @lcpr case=start
# []\n[0]\n
# @lcpr case=end

#

