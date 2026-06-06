class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sList = list(s)
        idxes = []
        for i, char in enumerate(t):
            if char not in sList:
                return False
            else:
                index = sList.index(char)
                sList.pop(index)
        return True
        