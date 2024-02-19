#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
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
            for r in self.combinationSumHelper(candidates, i+1, target - n):
                r.insert(0, n)
                results.append(r)
            i += 1
            while i<len(candidates) and candidates[i] == n:
                i += 1
            
        return results
    
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates = sorted(candidates)
        if target == 0 or not candidates or candidates[0] > target:
            return []
        return self.combinationSumHelper(candidates=candidates, start=0, target=target)
        
# @lc code=end

