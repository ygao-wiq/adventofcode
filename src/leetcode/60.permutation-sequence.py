#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#

# @lc code=start
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorials = [0 for i in range(n)]
        factorials[0] = 1
        for i in range(1, n):
            factorials[i] = factorials[i-1] * i
        nums = [i+1 for i in range(0, n)]

        k -= 1
        ret = []
        for i in range(n-1, -1, -1):
            idx = k // factorials[i]
            k -= idx * factorials[i]
            ret.append(str(nums[idx]))
            nums.remove(nums[idx])
        return "".join(ret)
# @lc code=end

if __name__ == "__main__":
    print(Solution().getPermutation(3,3))
    print(Solution().getPermutation(4,9))