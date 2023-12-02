class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        sign = 1
        sign_read = False
        whitespace_skipped = False
        ret = 0
        for c in s:
            if c.isspace() and not whitespace_skipped:
                continue
            elif (c == "-" or c == "+") and not sign_read:
                whitespace_skipped = True
                sign_read = True
                sign = 1 if c=="+" else -1
            elif c.isdigit():
                whitespace_skipped = True
                sign_read = True
                if ret > 214748364 or (ret == 214748364 and (sign>0 and int(c)>7 or sign<0 and int(c)>8)):
                    if sign == 1:
                        return 2147483647
                    else:
                        return -2147483648
                else:
                    ret = ret * 10 + int(c)
            else:
                break
        return ret * sign
    
if __name__ == "__main__":
    print(Solution().myAtoi("  00000-42a1234"))