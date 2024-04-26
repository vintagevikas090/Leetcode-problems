'''
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
'''

from typing import*

#   method 1

import heapq

class num:
    def __init__(self, data):
        self.data = data
    def __lt__(self, other):
        return self.data > other.data
    def __eq__(self, other):
        return self.data == other.data

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in nums:
            heapq.heappush(heap, num(i))
        
        i = 1
        while i < k:
            heapq.heappop(heap)
            i += 1

        return heap[0].data
    

# method 2
    import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums = [-i for i in nums]
        heap = []
        for i in nums:
            heapq.heappush(heap, -i)
        
        i = 1
        while i < k:
            heapq.heappop(heap)
            i += 1

        return - heap[0]