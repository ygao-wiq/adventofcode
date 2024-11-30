class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stk = []
        stk.append(-1)
        max_area = 0
        for i in range(len(heights)):
            while stk[-1] != -1 and heights[stk[-1]] >= heights[i]:
                current_height = heights[stk[-1]]
                stk.pop()
                current_width = i - stk[-1] -1
                max_area = max(max_area, current_height*current_width)
            stk.append(i)
            
        while stk[-1] != -1:
            current_height = heights[stk[-1]]
            stk.pop()
            current_width = len(heights) - stk.lastElement() - 1
            max_area = max(max_area, current_height * current_width)
        return max_area