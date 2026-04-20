class Solution:
    def maxArea(self, heights: List[int]) -> int:
        st, en = 0, len(heights) - 1
        mx = float('-inf')

        while st < en:
            l = min(heights[st], heights[en])
            b = en - st
            mx = max(l*b, mx)

            if heights[st] < heights[en]: st += 1
            else: en -= 1
            
        return mx