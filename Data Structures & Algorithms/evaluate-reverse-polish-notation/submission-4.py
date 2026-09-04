class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = 0
        if len(tokens) == 1: return int(tokens[0])
        stack=[]
        for i in tokens :
            if i == "+":
                op2 = stack.pop()
                op1 = stack.pop()
                result = op1 + op2
                stack.append(result)
            elif i == "-":
                op2 = stack.pop()
                op1 = stack.pop()
                result = op1 - op2
                stack.append(result)
            elif i == "*":
                op2 = stack.pop()
                op1 = stack.pop()
                result = op1 * op2
                stack.append(result)
            elif i == "/":
                op2 = stack.pop()
                op1 = stack.pop()
                result = int(op1 / op2)
                stack.append(result)
            else :
                stack.append(int(i))
        return result