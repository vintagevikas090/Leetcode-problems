'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some
 (can be none) of the characters without disturbing the relative positions of the remaining characters. 
 (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l = len(s)
        s_ptr = 0
        if len(s) == 0 :
            return True
        for i in t :
            # if ele is found in i, inc the s_ptr to point to the next char
            if i == s[s_ptr]:
                s_ptr += 1
            # if all ele were found, s_ptr will be equal to len(s)
            if s_ptr == l :
                return True
        return False