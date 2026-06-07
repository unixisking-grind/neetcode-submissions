class Solution:
    # Monotonic Decreasing Stack
    # We compare temp with top: temp < top
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for idx, temp in enumerate(temperatures):
            if not stack or temp < temperatures[stack[-1]]:
                stack.append(idx)
            else:
                while stack and temperatures[stack[-1]] < temp:
                    resIdx = stack.pop()
                    result[resIdx] = idx - resIdx


                stack.append(idx)
            print(f"temp is: {temp} and stack={stack} and result = {result}")
        return result


        

