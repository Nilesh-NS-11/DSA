"""

Find all Numbers Disappeared in an Array

Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]

"""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        output = []
        
        for n in nums:
            if nums[abs(n)-1] > 0:
                nums[abs(n)-1] = -nums[abs(n)-1]

        for i in range(len(nums)):
            if nums[i] > 0:
                output.append(i+1)
        
        return output
