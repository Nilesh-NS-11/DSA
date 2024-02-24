"""

Swapping Nodes in a Linked List

You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]
Example 2:

Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]
 

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        right_pointer = head
        for i in range(1,k):
            right_pointer = right_pointer.next
        left_kth_node = right_pointer

        left_pointer = head
        while right_pointer:
            right_kth_node = left_pointer
            left_pointer = left_pointer.next
            right_pointer = right_pointer.next
        
        left_kth_node.val, right_kth_node.val = right_kth_node.val, left_kth_node.val
        return head
        