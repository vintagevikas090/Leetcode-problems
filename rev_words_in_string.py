'''
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. 
The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        l = (s.split())
        new_str = ''
        for i in l[::-1]:
            new_str += i
            new_str += ' '
        new_str = new_str.strip()
        return new_str
    
# method 2

class Solution:
    def reverseWords(self, s: str) -> str:
        l = (s.split())
        return ' '.join(l[::-1])