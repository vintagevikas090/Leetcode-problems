'''
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

 

Example 1:


Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]
Example 2:


Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]
'''
from typing import *

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        cnt = 0
        
        freq1 = {}
        # count the freq of each sublist
        for lst in grid:
            t = tuple(lst)
            freq1[t] = freq1.get(t, 0) + 1
        

        # make the column_matrix
        # after making each col, check if that is present in freq1
        col_mat = []
        for j in range(n):
            l = []
            for i in range(n):
                l.append(grid[i][j])
            t = tuple(l)
            col_mat.append(t)
            cnt += freq1.get(t, 0)

        return cnt