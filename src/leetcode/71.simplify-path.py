#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split("/")
        ret = []
        for p in paths:
            if p == "." or not p or p == "/":
                continue
            elif p == "..":
                if len(ret) >= 1:
                    ret.pop(-1)
            elif p:
                ret.append(p)
        return "/" + "/".join(ret)
# @lc code=end

if __name__ == "__main__":
    input_path = "/.../a/../b/c/../d/./"
    print(Solution().simplifyPath(input_path))