class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = {}
        for char in s:
            map1[char] = map1.get(char, 0) + 1
        
        print(map1)
        for char in t:
            if char not in map1 or map1[char] == 0:
                print(char)
                return False
            map1[char] -= 1

        for key in map1.keys():
            if map1.get(key) != 0:
                return False
            
        return True
            

            

        
        
        

        
        