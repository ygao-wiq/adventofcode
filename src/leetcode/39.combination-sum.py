#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSumHelper(self, candidates: list[int], start: int, target: int) -> list[list[int]]:
        results = []
        if not candidates or candidates[0] > target:
            return []
        i = start
        while i<len(candidates):
            n = candidates[i]
            if n > target:
                return results
            if n == target:
                results.append([n])
            for r in self.combinationSumHelper(candidates, i, target - n):
                r.insert(0, n)
                results.append(r)
            i += 1
        return results
    
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates = sorted(candidates)
        if target == 0 or not candidates or candidates[0] > target:
            return []
        return self.combinationSumHelper(candidates=candidates, start=0, target=target)
    
# @lc code=end

if __name__ == "__main__":
    print(Solution().combinationSum([8,7,4,3], 11))