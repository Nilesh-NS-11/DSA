"""

Valid Anagram


Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false

"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        cntMapS, cntMapT = {}, {}
        
        for s1,s2 in zip(s,t):
            cntMapS[s1] = cntMapS.get(s1,0) + 1
            cntMapT[s2] = cntMapT.get(s2,0) + 1 

        for c in cntMapS:
            if cntMapT.get(c,0) != cntMapS[c]:
                return False
        
        return True
        