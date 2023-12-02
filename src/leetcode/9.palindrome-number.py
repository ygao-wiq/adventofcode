class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0 or (x>0 and x%10 == 0):
            return False
        
        reverted_num = 0
        while reverted_num<x:
            last_digit = x % 10
            x = x // 10
            reverted_num = reverted_num * 10 + last_digit
        return reverted_num == x or (reverted_num//10==x)