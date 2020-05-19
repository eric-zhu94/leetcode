https://leetcode.com/problems/check-if-it-is-a-straight-line/
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        #y = mx + b
        if len(coordinates) == 2:
            return True
        else:
            #m = (y1-y0) / (x1-x0)
            try:
                m = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
            except:
                m = None
            if m is None:
                if len(set([x[0] for x in coordinates])) == 1:
                    return True
                else:
                    return False
            #b = y- mx
            b = coordinates[1][1] - m * coordinates[1][0]
            for point in coordinates:
                if (point[1] - (m * point[0]) - b) != 0:
                    return False
            return True
                    
        
