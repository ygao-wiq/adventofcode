class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        roman_to_int_mapping = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }
        tmp_chars = list()
        for k in sorted(roman_to_int_mapping.keys(), reverse=True):
            if num < k:
                continue
            else:
                v = roman_to_int_mapping[k]
                tmp_chars.extend([v for i in range(num//k)])
                num = num % k
        return "".join(tmp_chars)
    
if __name__ == "__main__":
    print(Solution().intToRoman(58))