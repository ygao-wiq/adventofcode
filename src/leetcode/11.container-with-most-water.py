class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ret = 0
        left = 0
        right = len(height)-1
        while left < right:
            sz = min(height[left], height[right])*(right-left)
            ret = max(ret, sz)
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        return ret