class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seste = set ()
        for i in nums :
            if i in seste :
                return True 
            else :
                seste.add(i) 
            
        return False 
