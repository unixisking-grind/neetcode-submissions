class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        obj1 = {}
        obj2 = {}
        for char in s:
            if char not in obj1:
                obj1[char] = 1
            else:
                obj1[char] += 1
        for char in t:
            if char not in obj2:
                obj2[char] = 1
            else:
                obj2[char] += 1
        
        for key, value in obj1.items():
            if key not in obj2 or obj2[key] != value:
                return False

        return True
        

        