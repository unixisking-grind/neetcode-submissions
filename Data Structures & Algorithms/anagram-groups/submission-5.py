"""
M * N where n is the length of the longest string and M = number of strings
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        d = {}
        current_anagram = sorted(strs[0])
        for idx, word in enumerate(strs):
            sorted_word = "".join(sorted(word))
            if len(d) == 0:
                print(sorted_word)
                d[sorted_word] = [word]
            elif sorted_word in d:
                d[sorted_word].append(word)
            else:
                d[sorted_word] = [word]
        
        for key in d.keys():
            output.append(d[key])
        return output
