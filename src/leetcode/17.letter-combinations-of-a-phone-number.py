number_to_char = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}
class Solution(object):
    def helper(self, digits, start, temp, ret):
        """
        :type digits: str
        :type int: start
        :type List[str]: temp
        :type List[List[str]]
        :rtype: List[str]
        """
        if start == len(digits):
            ret.append("".join(temp))
        else:
            for c in number_to_char[digits[start]]:
                temp.append(c)
                self.helper(digits, start+1, temp[:], ret)
                temp = temp[:-1]
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ret = []
        if not digits:
            return ret
        for c in number_to_char[digits[0]]:
            temp = [c]
            self.helper(digits, 1, temp[:], ret)
        return ret
            
if __name__ == "__main__":
    print(Solution().letterCombinations(['2', '3', '4']))
    print(Solution().letterCombinations(['2', '3']))
    print(Solution().letterCombinations(['2']))
    print(Solution().letterCombinations([]))