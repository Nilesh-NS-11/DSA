"""

Rotate List

Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        old_head = head

        cur, size = head, 0
        while cur:
            cur, size = cur.next, size + 1

        if k % size == 0:
            return head

        k %= size
        slow, fast = head, head
        while fast and fast.next:
            if k <= 0:
                slow = slow.next
            fast = fast.next
            k -= 1
        
        new_tail, new_head, old_tail = slow, slow.next, fast
        new_tail.next = None
        old_tail.next = old_head

        return new_head

        