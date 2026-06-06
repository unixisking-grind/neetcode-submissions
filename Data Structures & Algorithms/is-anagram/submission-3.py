class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sValue = 0
        tValue = 0

        for char in s:
            sValue += ord(char)
        for char in t:
            tValue += ord(char)
        if tValue != sValue:
            return False
        for char in t:
            if char not in s:
                return False   
        return True
        