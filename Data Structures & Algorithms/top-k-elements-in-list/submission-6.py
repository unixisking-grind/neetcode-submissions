"""
loop through the nums

"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums
        obj = {}

        for i, num in enumerate(nums):
            if num in obj:
                obj[num] += 1
            else:
                obj[num] = 1

        occurencesList = [[]] * (len(nums) + 1)
        for key in obj.keys():
            valOccu = obj[key]
            if len(occurencesList[valOccu]) == 0:
                occurencesList[valOccu] = [key]
            else:
                occurencesList[valOccu].append(key)
        
        result = []
        for elements in reversed(occurencesList):
            if len(result) == k:
                break

            diff = k - len(result)
            if len(elements) == 0:
                continue
            else:
                for i in range(len(elements)):
                    result.append(elements[i])



        return result
            



        