class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxsums = nums[0]
        curent = 0 
        for i in range(len(nums)) :
            if  curent < 0 :
                curent = 0 
            curent += nums[i]
            maxsums = max (curent , maxsums)
        return maxsums 

# nums = [2,-3,4,-2,2,1,-1,4] 
            
# for i = 0   current = 2  ( curent +=nums[i])  maxsum = 2  
# for i = 1    curent = -1    

        


    
        