class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        i = 0
        opt_plst = list()
        prev = None
        while i < len(p):
            if i+1 < len(p) and p[i+1] == "*":
                if p[i] != prev:
                    prev = p[i]
                    opt_plst.extend(p[i:i+2])
                i += 2
                continue
            else:
                prev = None
                opt_plst.append(p[i])
                i += 1
                
        return self.helper(s, "".join(opt_plst))
    
    def helper(self, s, p):
        if len(p) == 0:
            return len(s) == 0
        first_match = len(s)>0 and (p[0] == "." or p[0] == s[0])
        if len(p) >= 2 and p[1] == "*":
            return self.helper(s, p[2:]) or (first_match and self.helper(s[1:], p))
        else:
            return first_match and self.helper(s[1:], p[1:])
    
if __name__ == "__main__":
    print(Solution().isMatch("a", "a*a*a*a*a*a*a*a*a*a*b"))