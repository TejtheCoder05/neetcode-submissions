class Solution:
    def isAnagram(self, s: str, t: str) -> bool: 
        countS = {}
        countT = {}

        if len(t) != len(s):
            return False
        
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
        
        for key in countS:
            if key not in countT:
                return False
            if countS[key] != countT[key]:
                return False
        
        return True
        