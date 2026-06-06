class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        size = len(temperatures)
        for i in range(size):
            found = False
            for j in range(i+1, size):
                if temperatures[j] > temperatures[i]:
                    result.append(j - i)
                    found = True
                    break

            if not found:
                result.append(0)
        return result
                    
                



        