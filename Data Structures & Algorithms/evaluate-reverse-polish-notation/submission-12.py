class Solution:
    def op(self,op1, op2, operation):
        match operation:
            case "+":
                return int(op1) + int(op2)
            case "-":
                return int(op1) - int(op2)
            case "*":
                return int(op1) * int(op2)
            case "/":
                return int(op1) / int(op2)

    def isOp(self, op):
        if op == '*' or op == '-' or op == '/' or op == '*' or op == '+':
            return True
        return False
        
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0
        
        i = len(tokens) - 1
        while i >= 0:
            stack.append(tokens[i])
            i = i - 1
        
        print(stack)
        cache = []
        while stack:
            result = stack.pop()
            if not stack:
                return int(result)
            operand = stack.pop()
            operator = stack.pop()
            while not self.isOp(operator):
                # Need to cache the result in another stack, do the operation and then put it back
                print("inside? ", operator)
                cache.append(result)
                result = operand
                operand = operator
                operator = stack.pop()
                print("cache",cache)
            

            result = self.op(result, operand, operator)
            stack.append(result)
            while cache:
                cached = cache.pop()
                stack.append(cached)
            print("stack after", stack)


        return result




        




        