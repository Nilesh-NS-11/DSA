"""

Sort Colors

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]


1. Count the number of 0s 1s and 2s put in map
2. Iterate through map and replace original array with number of 0s 1s and 2s from map.

for n in nums:
            cntMap[n] = cntMap.get(n,0) + 1
        k = 0
        for i in range(3):
            for j in range(cntMap[i]):
                nums[k] = i
                k += 1
				
1. Keep 2 pointers left and right.
2. Iterate through array and swap array with left if number is 0, swap array with right if number is 2.
				
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l , r = 0 , len(nums) - 1
        i = 0

        while i <= r:
            if nums[i] == 0:
                nums[i],nums[l] = nums[l],nums[i]
                l += 1
            elif nums[i] == 2:
                nums[i],nums[r] = nums[r],nums[i]
                r -= 1
                i -= 1
            i += 1