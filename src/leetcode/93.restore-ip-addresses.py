#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#

# @lc code=start
class Solution:
    def is_valid(self, segment: str) -> bool:
        if len(segment) == 0 or len(segment) > 3:
            return False
        return len(segment) == 1 if segment[0] == '0' else segment.isdigit() and 0 <= int(segment) <= 255
    
    def backtrack(self, s: str, segments: list[str], outputs: list[str], length: int, dots: int, prev_pos: int) -> None:
        if dots == -1 and prev_pos == length - 1:
            outputs.append('.'.join(segments))
            return
        elif dots == -1:
            return
        end_pos = min(length - 1, prev_pos + 4)
        for i in range(prev_pos + 1, end_pos+1):
            segment = s[prev_pos + 1:i+1]
            if self.is_valid(segment):
                segments.append(segment)
                self.backtrack(s, segments, outputs, length, dots - 1, i)
                segments.pop()

    def restoreIpAddresses(self, s: str) -> list[str]:
        segments = []
        outputs = []
        n = len(s)
        dots = 3
        self.backtrack(s, segments, outputs, n, dots, -1)
        return outputs

        
# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.restoreIpAddresses("25525511135"))  # Example usage
    # print(solution.restoreIpAddresses("0000"))          # Example usage
    # print(solution.restoreIpAddresses("101023"))        # Example usage
    # print(solution.restoreIpAddresses("010010"))        # Example usage
    # print(solution.restoreIpAddresses("19216811"))      # Example usage
