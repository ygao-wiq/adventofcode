class Solution:
    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        
    def reverse(self, nums, i, j):
        while i<j:
            self.swap(nums, i, j)
            i += 1
            j -= 1
            
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        k = len(nums) - 2
        while k>=0 and nums[k]>=nums[k+1]:
            k -= 1
        if k >= 0:
            j = len(nums) -1
            while nums[j] <= nums[k]:
                j -= 1
            self.swap(nums, k, j)
        self.reverse(nums, k+1, len(nums)-1)

if __name__ == "__main__":
    Solution().nextPermutation([3,2,1])
    print("done")