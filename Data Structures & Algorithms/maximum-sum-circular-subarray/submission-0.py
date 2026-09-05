class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        Max , Min = nums[0], nums[0]
        currMax , currMin = 0,0 
        total = 0 
        for n in nums :
            currMax = max (currMax + n , n )
            currMin = min ( currMin + n , n )
            total += n 
            Max = max ( currMax , Max )
            Min = min ( currMin , Min )
            
        return max ( Max , total - Min) if Max > 0 else Max 
        
       