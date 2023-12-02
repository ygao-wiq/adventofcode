class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1
        ret = 0
        if x < 0:
            sign = -1
            x = x*-1
        while x>0:
            last_digit = x % 10
            if ret > 214748364 or (ret == 214748364 and (sign>0 and last_digit>7 or sign<0 and last_digit>8)):
                    return 0
            ret = ret * 10 + last_digit
            x = x / 10
        return ret * sign