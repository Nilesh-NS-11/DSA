"""

Sort List

Given the head of a linked list, return the list after sorting it in ascending order.

 

Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        mid = self.getMid(head)
        left, right = self.sortList(head), self.sortList(mid)

        return self.merge_two_sorted(left, right)
    
    def merge_two_sorted(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        ret = ListNode()
        prev = ret

        while list1 and list2:
            if list1.val < list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next
        
        if list1:
            prev.next = list1
        else:
            prev.next = list2
        
        return ret.next



    def getMid(self,head: Optional[ListNode]) -> Optional[ListNode]:
        mid_prev = None
        while head and head.next:
            mid_prev = mid_prev.next if mid_prev else head
            head = head.next.next
        
        mid = mid_prev.next
        mid_prev.next = None
    
        return mid


        