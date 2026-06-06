class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Monotonic strictly decreasing stack
        stack = []
        result = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while len(stack) > 0 and temp > temperatures[stack[-1]]:
                element = stack.pop()
                result[element] = i - element
            stack.append(i)

        return result