"""
M * N where n is the length of the longest string and M = number of strings
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        hset = {}
        current_anagram = sorted(strs[0])
        for idx, word in enumerate(strs):
            sorted_word = "".join(sorted(word))
            if len(hset) == 0:
                print(sorted_word)
                hset[sorted_word] = [word]
            elif sorted_word in hset:
                hset[sorted_word].append(word)
            else:
                hset[sorted_word] = [word]
            
        
        for key in hset.keys():
            output.append(hset[key])
        return output
