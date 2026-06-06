class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        obj = {}
        # Monotonic strictly decreasing stack
        stack = []
        result = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            if len(stack) == 0 or temperatures[stack[-1]] > temp:
                stack.append(i)
            else:
                while len(stack) > 0 and temp > temperatures[stack[-1]]:
                    element = stack.pop()
                    result[element] = i - element
                stack.append(i)
            print(stack)

        return result





        