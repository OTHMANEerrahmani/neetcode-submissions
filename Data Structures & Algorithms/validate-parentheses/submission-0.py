class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mach={")":"(","}":"{","]":"["}
        for i in s :
            if i in "({[":
                stack.append(i)
            elif not stack :
                    return False 
            elif stack[-1]== mach[i]:
                    stack.pop()
            else: return False
        return len(stack)==0
   