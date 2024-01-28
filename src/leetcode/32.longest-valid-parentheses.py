
class Solution(object):
    def longestValidParenthesesStack(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = list()
        stack.append(-1)
        ans = 0
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                ans = max(ans, i-stack[-1])
        return ans
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0 for i in range(len(s))]
        ans = 0
        for i, c in enumerate(s):
            if c == ")":
                if i>0 and s[i-1]=="(":
                    dp[i] = (dp[i-2] if i>=2 else 0) + 2
                elif i>0 and i - dp[i-1] > 0 and s[i-dp[i-1]-1]=="(":
                    dp[i] = dp[i-1] + (dp[i-dp[i-1]-2] if (i-dp[i-1]) >= 2 else 0) + 2
                ans = max(ans, dp[i])
        return ans
    
if __name__ == "__main__":
    print(Solution().longestValidParentheses(")()())"))
    print(Solution().longestValidParentheses(""))
            