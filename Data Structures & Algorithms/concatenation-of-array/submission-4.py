class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        

        ans = [0] * len(2 * nums)

        for i in range(len(ans)): 
            if i >= len(nums): 
                ans[i] = nums[i-len(nums)] 
            else: 
                ans[i] = nums[i] 
        
        return ans 

        
        
