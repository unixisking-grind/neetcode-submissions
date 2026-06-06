class Solution:
    def isMatch(self, s1:str, s2: str) -> bool:
        if s1 == '(' and s2 == ')':
            return True
        elif s1 == '{' and s2 == '}':
            return True
        elif s1 == '[' and s2 == ']':
            return True
        return False
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '[' or char == '(' or char == '{':
                stack.append(char)
                continue
            elif len(stack) == 0:
                return False
            if self.isMatch(stack[-1],char):
                stack.pop() 
            else:
                return False
        
        return len(stack) == 0





        
        