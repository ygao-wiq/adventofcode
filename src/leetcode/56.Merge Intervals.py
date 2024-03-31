class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        ans = []
        for e in intervals:
            if not ans or e[0]>ans[-1][1]:
                ans.append(e)
            elif e[1] > ans[-1][1]:
                ans[-1][1] = e[1]    
        return ans
        
if __name__ == "__main__":
    print(Solution().merge([[2,6],[1,3],[8,10],[15,18]]))