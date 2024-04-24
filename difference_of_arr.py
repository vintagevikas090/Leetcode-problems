'''
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.

 

Example 1:

Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]
Explanation:
For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6]
'''
from typing import *

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        '''Method 1'''
        # res1 = set()
        # for val in nums1:
        #     if val not in nums2:
        #         res1.add(val)

        # res2 = set()
        # for num in nums2:
        #     if num not in nums1:
        #         res2.add(num)

        # ans = []
        # ans.append(list(res1))
        # ans.append(list(res2))
        # return ans


        '''Method 2'''
        # freq1 = {}
        # for val in nums1:
        #     if val in freq1:
        #         freq1[val] += 1
        #     else:
        #         freq1[val] = 1

        # freq2 = {}
        # for i in nums2:
        #     if i in freq2:
        #         freq2[i] += 1
        #     else:
        #         freq2[i] = 1

        # res1 = set()
        # for i in nums2:
        #     if i not in freq1:
        #         res1.add(i)

        # res2 = set()
        # for i in nums1:
        #     if i not in freq2:
        #         res2.add(i)

        # return [list(res2), list(res1)]


        '''Method 3'''
        res1 = set(nums1) - set(nums2)
        res2 = set(nums2) - set(nums1)
        return [list(res1), list(res2)]