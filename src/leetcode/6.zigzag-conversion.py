class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or len(s) == 0:
            return s
        ret = list()
        row = 0
        inc = 1
        for c in s:
            if len(ret) < row+1:
                ret.append(list())
            ret[row].append(c)
            row = row + inc
            if row == numRows-1 or row == 0:
                inc = -1 * inc
                    
        ret_str = ""
        for row in ret:
            ret_str += "".join(row)
        return ret_str
    
if __name__ == "__main__":
    print(Solution().convert("PAYPALISHIRING", 3))