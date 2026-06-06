class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sSet = set(s)
        for char in sSet:
            if s.count(char) != t.count(char):
                return False
        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        n = len(strs)

        for i in range(n):
            firstWord = strs[i]
            print(f"{i} ${firstWord}")
            isIncluded = False
            for x in range(len(result)):
                if firstWord in result[x]:
                    isIncluded = True

            if isIncluded == False:
                tmp = []
                for j in range(i+1, n):
                    secondWord = strs[j]
                    print(f"j={j} {secondWord}")
                    """
                    if firstWord == secondWord:
                        print(f"i={i} and j={j}, {firstWord} {secondWord}")
                        """
                    if self.isAnagram(firstWord, secondWord):
                        tmp.append(secondWord)
                tmp.append(firstWord)
                result.append(tmp)

        return result
                



            


        
        