class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 

        anagram = {}
        anagram2 = {} 

        for i in range(len(s)): 
            anagram[s[i]] = anagram.get(s[i], 0) + 1  
        
        for i in range(len(t)): 
            anagram2[t[i]] = anagram2.get(t[i], 0) + 1  
        

        return (anagram == anagram2)
       

  
            
            