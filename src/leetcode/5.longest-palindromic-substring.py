class Solution(object):
    def helper(self, s, start, curr_len):
        ret1=0
        ret2=0
        if start % 2 == 1:
            i = (start+1)//2-1
            j = (start+1)//2
            if 2*min(i-0+1, len(s)-j) < curr_len:
                if s[i] == s[j]:
                    return i, j
                else:
                    return 0, 0
        else:
            i = start // 2
            j = start // 2
            if 2*min(i-0+1, len(s)-j-1) < curr_len:
                return i, j

        while i>=0 and j< len(s) and s[i] == s[j]:
            ret1 = i
            ret2 = j
            i = i-1
            j = j+1
        return ret1, ret2

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = 0
        end = 0
        for k in range(2*(len(s)-1)+1):
            i, j = self.helper(s, k, (end-start+1))
            if (j-i+1) > (end-start+1):
                start = i
                end = j
        return s[start:end+1]

if __name__ == "__main__":
    print(Solution().longestPalindrome("babad"))