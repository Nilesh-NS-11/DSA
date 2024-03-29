"""

Largest Number

Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

 

Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"

"""

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        
        def comp(n1,n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1
            
        nums = sorted(nums,key=cmp_to_key(comp))

        return str(int("".join(nums)))
        