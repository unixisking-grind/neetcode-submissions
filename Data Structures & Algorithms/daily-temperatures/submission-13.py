class Solution:
    # Monotonic decreasing Stack
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for idx, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                resIdx = stack.pop()
                result[resIdx] = idx - resIdx

            stack.append(idx)
        return result


        

