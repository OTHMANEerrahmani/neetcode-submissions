class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m=0
        k=0
        for i in nums :
            if i==1:
                k+=1
            else:
                m=max(m,k)
                k=0
        return max(k,m)