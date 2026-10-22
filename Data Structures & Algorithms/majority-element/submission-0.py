class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        majority = {} 

        for i in range(len(nums)): 
            majority[nums[i]] = majority.get(nums[i], 0) + 1
        

        highest = 1 
        for key in majority: 
            if majority[key] > highest: 
                highest = majority[key]
       
        for key in majority: 
            if majority[key] == highest:
                return key 