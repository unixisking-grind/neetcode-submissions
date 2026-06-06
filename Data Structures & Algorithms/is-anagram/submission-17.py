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

        for c in s:
            if c in dictOne:
                dictOne[c] += 1
            else:
                dictOne[c] = 1
        for c in t:
            if c in dictTwo:
                dictTwo[c] += 1
            else:
                dictTwo[c] = 1
        for key in dictOne.keys():
            if key not in dictTwo or dictOne[key] != dictTwo[key]:
                return False
        return True

        


        