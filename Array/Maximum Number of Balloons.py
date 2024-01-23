"""

Maximum Number of Balloons

Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

Example 1:



Input: text = "nlaebolko"
Output: 1
Example 2:



Input: text = "loonbalxballpoon"
Output: 2

"""

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        mincntMap = {'b':1, 'a':1, 'l':2,'o':2,'n':1}
        cntMap = {}
        res = float("inf")

        for n in text:
            cntMap[n] = cntMap.get(n,0) + 1
        
        
        for k in mincntMap:
            if k not in cntMap:
                return 0
            res = min(cntMap[k]//mincntMap[k],res)
        
        return res
            


