class Solution(object):
    def romanToInt(self, roman):
        """
        :type roman: str
        :rtype: int
        """
        
        roman_to_int_mapping = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1
        }
        ret = 0
        while roman:
            for k in ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]:
                if roman.startswith(k):
                    ret += roman_to_int_mapping[k]
                    roman = roman[len(k):]
        return ret

if __name__ == "__main__":
    print(Solution().romanToInt("IV"))