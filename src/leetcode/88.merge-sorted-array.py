#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = []
        i, j = 0, 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                temp.append(nums1[i])
                i += 1
            else:
                temp.append(nums2[j])
                j += 1
        while i < m:
            temp.append(nums1[i])
            i += 1
        while j < n:
            temp.append(nums2[j])
            j += 1
        nums1.clear()
        nums1.extend(temp)
        
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    s.merge(nums1, m, nums2, n)
    print(nums1)  # Output: [1, 2, 2, 3, 5, 6]