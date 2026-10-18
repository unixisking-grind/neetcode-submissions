class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sorted_nums = sorted(nums)
        result = defaultdict(int)

        for num in nums:
            result[num] += 1

        sorted_result = [k for k,v in sorted(result.items(), key=lambda item: item[1])]

        """
        output = []
        i = len(sorted_result) - 1
        while i >= 0 and k>0:
            output.append(sorted_result[i])
            i -= 1
            k -= 1
        """
        return  sorted_result[len(sorted_result)-k:len(sorted_result)]
            


        