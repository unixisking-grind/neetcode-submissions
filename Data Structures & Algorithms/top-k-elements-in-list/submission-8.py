"""
loop through the nums

"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums
        obj = Counter(nums) # This counts like this : {number: NumOfOccurences}

        occurencesList = [[] for _ in range(len(nums) + 1)]

        for num, count in obj.items():
            occurencesList[count].append(num)

        result = []
        for elements in reversed(occurencesList):
            if len(result) == k:
                break

            diff = k - len(result)
            if len(elements) == 0:
                continue
            else:
                for i in range(len(elements)):
                    if i >= diff:
                        break
                    result.append(elements[i])



        return result
            



        