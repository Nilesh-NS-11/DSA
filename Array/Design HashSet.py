"""
Design HashSet


Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
 

Example 1:

Input
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output
[null, null, null, true, false, null, true, null, false]
"""

class ListNode:

    def __init__(self,key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.set = [ListNode(0) for _ in range(10**4)]
        
    def _hashKey(self,key):
        return key % (10**4)

    def add(self, key: int) -> None:
        idx = self._hashKey(key)
        curr = self.set[idx]
        while curr.next:
            if curr.next.key == key:
                return
            curr = curr.next
        curr.next = ListNode(key)


    def remove(self, key: int) -> None:
        idx = self._hashKey(key)
        curr = self.set[idx]
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next

        

    def contains(self, key: int) -> bool:
        idx = self._hashKey(key)
        curr = self.set[idx]
        while curr.next:
            if curr.next.key == key:
                return True
            curr = curr.next
        return False

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)