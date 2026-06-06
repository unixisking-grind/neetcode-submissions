class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True

        stack = []
        opening = ['[', '{', '(']

        for char in s:
            try:
                if char in opening:
                    stack.append(char)
                elif char == ')':
                    popped = stack.pop()
                    if popped != '(':
                        return False
                        
                elif char == ']':
                    popped = stack.pop()
                    if popped != '[':
                        return False
                elif char == '}':
                    popped = stack.pop()
                    if popped != '{':
                        return False
                else:
                    return False
            except:
                return False

        if len(stack) == 0:
            return True

        return False