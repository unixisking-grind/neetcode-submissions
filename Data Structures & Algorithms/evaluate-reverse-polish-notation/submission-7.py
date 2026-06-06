class Solution:
    def isOp(self, token: str) -> bool:
        ops = ['+', '-', '*', '/']
        return True if token in ops else False
    def operation(self, op: str, operandOne: int, operandTwo: int) -> int:
        match op:
            case '+':
                return operandOne + operandTwo
            case '-':
                return operandOne - operandTwo
            case '*':
                return operandOne * operandTwo
            case '/':
                return int(operandOne/operandTwo)

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        while tokens:
            token = stack.append(tokens.pop())
        
        result = None
        cache = []

        while stack:
            token = stack.pop()
            if self.isOp(token):
                # do some work
                if result is None:
                    operandTwo = cache.pop()
                    operandOne = cache.pop()
                    print(f"here {operandOne}, {operandTwo} op: {token}")
                    cache.append(self.operation(token, operandOne, operandTwo))
                else:
                    operandTwo = cache.pop()
                    operandOne = cache.pop()
                    print(f"here {operandOne}, {operandTwo} op: {token}")
                    cache.append(self.operation(token, operandOne, operandTwo))
            else:
                try:
                    cache.append(int(token))
                except:
                    raise Exception(f"Unrecognized token ! token={token}")
                
        if len(cache) != 1:
            raise Exception(f"Parsing is wrong !")

        return cache.pop()
