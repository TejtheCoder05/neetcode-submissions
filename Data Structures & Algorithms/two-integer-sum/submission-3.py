class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
      

        sum = {}  

        for i in range(len(nums)): 
            complement = target - nums[i] 
            if complement in sum: 
                return [sum[complement], i] 
            else: 
                sum[nums[i]] = i 

