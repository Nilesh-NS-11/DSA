"""

Word Pattern

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false

"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern) != len(s.split(" ")):
            return False
        
        mapPtoS , mapStoP = {} , {}

        for p,s in zip(pattern,s.split(" ")):
            if p in mapPtoS and mapPtoS[p] != s:
                return False
            if s in mapStoP and mapStoP[s] != p:
                return False
            mapPtoS[p] = s
            mapStoP[s] = p
        
        return True
       
        