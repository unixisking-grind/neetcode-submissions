class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Map(char -> 4) k = 5
        """
        hashmap = dict()
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
            
        hashmap = {k: v for k, v in sorted(hashmap.items(), key=lambda item: item[1],reverse=True)}

        return list(hashmap.keys())[:k]

        

        