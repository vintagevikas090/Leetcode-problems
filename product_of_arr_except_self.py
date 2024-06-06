'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all
 the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''

from typing import *

# res[i] = prefix_arr[i] * suffix_arr[i]
# suffix -->> rev of (prefix of (rev of nums))

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        pre = 1
        prefix = []
        for i in nums:
            prefix.append(pre)
            pre = pre * i

        suf = 1
        suffix = []
        for i in nums[::-1]:
            suffix.append(suf)
            suf = suf * i
        
        res = [1] * n
        for i in range(n):
            res[i] = prefix[i] * suffix[::-1][i]

        return res
        