#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ret = dict()
        if not strs:
            return []
        for s in strs:
            count = [0 for _ in range(26)]
            for c in s:
                count[ord(c)-97] += 1
            key = "#".join([str(c) for c in count])
            if key not in ret:
                ret[key] = []
            ret[key].append(s)
        return ret.values()

            
        
# @lc code=end
