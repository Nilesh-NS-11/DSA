"""

Find All Anagrams in a String

Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        countS, countP = {}, {}

        for i in range(len(p)):
            countP[p[i]] = countP.get(p[i],0) + 1
            countS[s[i]] = countS.get(s[i],0) + 1
        
        res = [0] if countP == countS else []
        l = 0
        for r in range(len(p),len(s)):
            countS[s[r]] = countS.get(s[r],0) + 1
            countS[s[l]] -= 1

            if countS[s[l]] == 0:
                countS.pop(s[l])
            l += 1
            if countP == countS:
                res.append(l)
            
            
        return res
        