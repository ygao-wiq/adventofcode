import sys
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        nums = sorted(nums)
        diff = sys.maxsize
        for i, num in enumerate(nums):
            if diff == 0:
                break
            lo = i+1
            hi = len(nums)-1
            while lo < hi:
                sum = nums[i] + nums[lo] + nums[hi]
                if abs(sum-target) < abs(diff):
                    diff = sum-target
                if sum > target:
                    hi -= 1
                else:
                    lo += 1
        return target + diff
    
if __name__ == "__main__":
    print(Solution().threeSumClosest([-1,2,1,-4], 1))
    print(Solution().threeSumClosest([0,1,2], 3))