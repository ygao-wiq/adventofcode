class Solution(object):
    def twoSum(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: List[List[int]]
        """
        ret = list()
        if start >= len(nums)-1:
            return ret
        lo = start
        hi = len(nums) -1
        while lo < hi:
            sum = nums[lo] + nums[hi]
            if sum == target:
                ret.append([nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo-1] == nums[lo]:
                    lo += 1
            elif sum < target:
                lo += 1
            else:
                hi -= 1
        return ret
    
    def kthSum(self, nums, target, start, k):
        """
        :type nums: List[int]
        :type target: int
        :type k: int
        :rtype: List[List[int]]
        """
        ret = list()
        if start+k > len(nums):
            return ret
        if nums[start]*k > target or nums[-1]*k < target:
            return ret
        if k == 2:
            return self.twoSum(nums, target, start)
        i = start
        while i<=len(nums)-k:
            if i == start or nums[i] != nums[i-1]:
                for subset in self.kthSum(nums, target-nums[i], i+1, k-1):
                    ret.append([nums[i]] + subset)
            i += 1
        return ret
        
    
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        return self.kthSum(nums, target, 0, 4)
    
if __name__ == "__main__":
    print(Solution().fourSum([1,0,-1,0,-2,2], 0))
    print(Solution().fourSum([2,2,2,2], 8))