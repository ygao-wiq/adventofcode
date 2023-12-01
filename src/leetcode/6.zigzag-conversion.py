class Solution(object):
    def convert1(self, s, numRows):
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
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or len(s) == 0:
            return s
        ret = list()
        doubleLen = 2*numRows - 2
        i = 0
        while i<numRows:
            j = 0
            while i+j < len(s):
                ret.append(s[i+j])
                if i != 0 and i != numRows-1 and j+doubleLen-i < len(s):
                    ret.append(s[j+doubleLen-i])
                j = j+ doubleLen
            i += 1
        return "".join(ret)

if __name__ == "__main__":
    print(Solution().convert("PAYPALISHIRING", 3))