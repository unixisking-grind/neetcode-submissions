class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sorted_nums = sorted(nums)
        result = defaultdict(int)
        for num in nums:
            result[num] += 1

        sorted_result = [k for k,v in sorted(result.items(), key=lambda item: item[1])]
        length = len(sorted_result)
        return  sorted_result[length-k:length]
            


        