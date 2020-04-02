class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        if len(points) <=1:
            return 0
        else:
            ptr = 0
            ans = 0
            while ptr != len(points) - 1:
                ans += max(abs(points[ptr][0] - points[ptr+1][0]),abs(points[ptr][1] - points[ptr+1][1]))
                ptr += 1
            return ans
        
