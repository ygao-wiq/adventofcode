class Solution:
    def myPow(self, x: float, n: int) -> float:
        N = n
        ans = 1.0
        if N < 0:
            N = -N
            x = 1/x
        current = x
        i = N
        while i>0:
            if i%2 == 1:
                ans *= current
            current *= current
            i //= 2
        return ans
    
if __name__ == "__main__":
    print(Solution().myPow(2.0, 10))