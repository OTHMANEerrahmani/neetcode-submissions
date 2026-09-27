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