"""

Number of Zero-Filled Subarrays

Given an integer array nums, return the number of subarrays filled with 0.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,3,0,0,2,0,0,4]
Output: 6
Explanation: 
There are 4 occurrences of [0] as a subarray.
There are 2 occurrences of [0,0] as a subarray.
There is no occurrence of a subarray with a size more than 2 filled with 0. Therefore, we return 6.
Example 2:

Input: nums = [0,0,0,2,0,0]
Output: 9
Explanation:
There are 5 occurrences of [0] as a subarray.
There are 3 occurrences of [0,0] as a subarray.
There is 1 occurrence of [0,0,0] as a subarray.
There is no occurrence of a subarray with a size more than 3 filled with 0. Therefore, we return 9.

"""

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        l,r = 0,0
        count = 0
        while r < len(nums):
            if nums[r] == 0:
                l = r
                while r < len(nums) and nums[r] == 0:
                    r += 1
                count += ((r-l) * (r-l+1))//2
            r += 1
        
        return count
                

        

        