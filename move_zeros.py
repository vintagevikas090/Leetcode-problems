'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
'''
from typing import *

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return
        
        # cnt = 0
        # left = 0
        # while left < len(nums):
        #     if nums[left] == 0:
        #         cnt += 1
        #         nums.remove(nums[left])
        #     else:
        #         left += 1
        
        # for i in range(cnt):
        #     nums.append(0)


        # Optimised approach
        
        slow = 0
        for fast in range(len(nums)):
            # swap is only done if slow ptr is at 0 
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            if nums[slow] != 0:
                slow += 1