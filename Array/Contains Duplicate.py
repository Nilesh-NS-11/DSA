"""

Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false

"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cntSet = set()

        for n in nums:
            if n in cntSet:
                return True
            cntSet.add(n)
        
        return False
        