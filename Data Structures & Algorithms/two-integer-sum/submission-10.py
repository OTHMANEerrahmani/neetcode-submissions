class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}
        for i , num in enumerate (nums):
            need = target - num 
            if need in index :
                return [index[need], i]
            index[num] = i 
















        # L = 0 
        # R = len(nums)-1
        # while L < R :
        #     need = nums [R ] + nums [L]
        #     if need == target :
        #         return [L,R]
        #     elif need > target :
        #         R -=1 
        #     else :
        #         L +=1  
        
            




        





        # # use hashMap 
        # index = {}

        # # use enumerat and go througth the nums 
        # for i , num in enumerate (nums):
        #      # i'm gonna cheek if target - nums in hashMap 
        #      need = target - num 
        #      if  need in index :
        #         return [index[need], i]
        #      index[num] = i 
            
        


       

        # if yes I need to return the indes of i and the indec of hashmap 
        # if no I'm gonna add the num to hashmap 









        # I need to aske some question 
        # first one : what if we don't find what we looking for what should I return )? 
        # is the array sorted or not 
        # for i in range (len(nums)-1):
              # for j in range (i+1 , len(nums))


        