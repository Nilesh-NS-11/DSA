"""
Sort an array

Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

 

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).

class Solution:
	def sortArray(self, nums: List[int]) -> List[int]:
		def mergeSort(nums):
			if len(nums) > 1:
				mid = len(nums) // 2
				L = nums[:mid]
				R = nums[mid:]
				
				mergeSort(L)
				mergeSort(R)

				i = j = k = 0

                		while i < len(L) and j < len(R): 
		                    if L[i] < R[j]: 
                		        nums[k] = L[i] 
		                        i+=1
                		    else: 
		                        nums[k] = R[j] 
                		        j+=1
		                    k+=1
    
                		while i < len(L): 
		                    nums[k] = L[i] 
                		    i+=1
		                    k+=1

                		while j < len(R): 
		                    nums[k] = R[j] 
                		    j+=1
		                    k+=1
        
        mergeSort(nums)
        return nums
"""


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def mergeSort(nums):
            print("Merge Sort called for:")
            print(nums) 
            if len(nums) > 1: 
                mid = len(nums)//2
                L = nums[:mid] 
                R = nums[mid:] 

                mergeSort(L)
                mergeSort(R)

                print("Now merging")
                print(nums)
                print(L)
                print(R)

                i = j = k = 0

                while i < len(L) and j < len(R): 
                    if L[i] < R[j]: 
                        nums[k] = L[i] 
                        i+=1
                    else: 
                        nums[k] = R[j] 
                        j+=1
                    k+=1
    
                while i < len(L): 
                    nums[k] = L[i] 
                    i+=1
                    k+=1

                while j < len(R): 
                    nums[k] = R[j] 
                    j+=1
                    k+=1
        
        mergeSort(nums)
        return nums

        














