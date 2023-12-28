class Solution(object):
    def twoSums(self, nums, start, target, results):
        """
        :type nums: List[int]
        :type start: int
        :type target: int
        :type results: List[List[int]]
        :rtype: List[List[int]]
        """
        lo = start
        hi = len(nums)-1
        while lo < hi:
            if nums[lo] + nums[hi] == target:
                results.append([nums[start-1], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo<hi and nums[lo] == nums[lo-1]:
                    lo += 1
            elif nums[lo] + nums[hi] < target:
                lo += 1
            else:
                hi -= 1
                
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        ret = list()
        for i, num in enumerate(nums):
            if num > 0:
                break
            if i == 0 or nums[i] != nums[i-1]:
                self.twoSums(nums, i+1, 0-num, ret)
        return ret
    
if __name__ == "__main__":
    print(Solution().threeSum([-1,0,1,2,-1,-4]))