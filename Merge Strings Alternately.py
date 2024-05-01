'''
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, 
starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
'''

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)

        if l1 == 0:
            return word2
        if l2 == 0:
            return word1

        ptr1 = 0
        ptr2 = 0
        new_str = ''
        while ptr1 < l1 and ptr2 < l2:
            new_str += word1[ptr1]
            new_str += word2[ptr2]
            ptr1 += 1
            ptr2 += 1

        if ptr1 < l1:
            new_str += word1[ptr1:]
        
        if ptr2 < l2:
            new_str += word2[ptr2:]

        return new_str
