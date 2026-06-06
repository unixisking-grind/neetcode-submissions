class Solution:
    """
    return true if both strings have the same exact characters as another
    {
        "c":  3
        "b": 4
    }
    {
        "c":  3
        "b": 4
    }
    """
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dictOne = {}
        dictTwo = {}

        for i in range(len(s)):
            dictOne[s[i]] = 1 + dictOne.get(s[i], 0)
            dictTwo[t[i]] = 1 + dictTwo.get(t[i], 0)
        print(dictOne)
        print(dictTwo)
        return dictOne == dictTwo

        


        