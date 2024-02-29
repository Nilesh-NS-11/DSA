"""

Partition List


Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

 

Example 1:


Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Example 2:

Input: head = [2,1], x = 2
Output: [1,2]

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lt_list, ge_list = ListNode(-1), ListNode(-1)
        lt_dummy, ge_dummy = lt_list, ge_list
        while head:
            if head.val < x:
                lt_dummy.next = head
                lt_dummy = lt_dummy.next
            else:
                ge_dummy.next = head
                ge_dummy = ge_dummy.next
            head = head.next
        
        lt_dummy.next = ge_dummy.next = None
        lt_dummy.next = ge_list.next
        return lt_list.next
        