class Solution:
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]

        result = []
        for word in strs:
            if len(result) == 0:
                result.append([word])
            else:
                found = 0
                for sub_list in result:
                    if self.isAnagram(word, sub_list[0]):
                        sub_list.append(word)
                        found = 1
                
                if found == 0:
                    result.append([word])
                

        return result

        