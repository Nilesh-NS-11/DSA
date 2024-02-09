"""

132 Pattern

Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.

 

Example 1:

Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.
Example 2:

Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
Example 3:

Input: nums = [-1,3,2,0]
Output: true
Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].

"""

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        cur_min = nums[0]

        for n in nums:
            while stack and stack[-1][0] <= n:
                stack.pop()
            if stack and n < stack[-1][0] and n > stack[-1][1]:
                return True
            
            stack.append([n,cur_min])
            cur_min = min(cur_min,n)

        return False
        