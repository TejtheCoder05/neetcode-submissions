class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 
        countS = defaultdict(int)  # -> dictionary
        countT = defaultdict(int) 

        if len(s) != len(t): 
            return False 
        
        for i in range(len(s)): 
            countS[s[i]] += 1 
            countT[t[i]] += 1 
        
        for key in countS: 
            if key not in countT: 
                return False  
            if countS[key] != countT[key]: 
                return False 
       
        return True 