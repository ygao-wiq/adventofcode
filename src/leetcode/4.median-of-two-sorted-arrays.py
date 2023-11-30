class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        nums1_len, nums2_len = len(nums1), len(nums2)
        odd_even = (nums1_len + nums2_len) % 2
        left = 0
        right = nums1_len

        while left <= right:
            partition_nums1 = (left + right) // 2
            partition_nums2 = (nums1_len + nums2_len + 1) // 2 - partition_nums1
            maxLeftA = -1 if partition_nums1 == 0 else nums1[partition_nums1-1]
            minRightA = 100000000 if partition_nums1 == nums1_len else nums1[partition_nums1]
            maxLeftB = -1 if partition_nums2 == 0 else nums2[partition_nums2-1]
            minRightB = 100000000 if partition_nums2 == nums2_len else nums2[partition_nums2]
            
            if max(maxLeftA, maxLeftB) <= min(minRightA, minRightB):
                if odd_even:
                    return max(maxLeftA, maxLeftB)
                else:
                    return (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2
            else:
                if maxLeftA > minRightB:
                    right = partition_nums1 - 1
                else:
                    left = partition_nums1 + 1

