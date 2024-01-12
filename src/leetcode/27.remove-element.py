#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        last = len(nums)
        prev = -1
        i = 0
        while i<last:
            if nums[i] != val:
                prev += 1
                nums[prev] = nums[i]
            else:
                last = last - 1
                while last>i and nums[last] == val:
                    last = last -1
                temp = nums[last]
                nums[last]= nums[i]
                prev += 1
                nums[prev] = temp
            i += 1
        return last
                
        
# @lc code=end

if __name__ == "__main__":
    print(Solution().removeElement([0,1,2,2,3,0,4,2], 2))
