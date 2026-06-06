class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashmap = {}
        
        for c in s:
            if c not in hashmap.keys():
                hashmap[c] = 1
            else:
                hashmap[c] += 1

        for c in t:
            if c in hashmap.keys():
                hashmap[c] -= 1
            else:
                return False
                
        for key in hashmap.keys():
            if hashmap[key] != 0:
                return False
        return True
        
        
        return True


        