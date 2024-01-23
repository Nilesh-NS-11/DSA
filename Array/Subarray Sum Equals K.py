"""
Subarray Sum Equals K

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2

"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sumMap = {}
        sum = 0
        sumMap[0] = 1 
        for n in nums:
            sum += n
            if sum - k in sumMap:
                count += sumMap[sum-k]
            sumMap[sum] = sumMap.get(sum,0) + 1

        return count

        
