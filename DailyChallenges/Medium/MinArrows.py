class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        maxp = points[0][1]
        ans = 0
        for i in points[1:]:
            if i[0] > maxp:
                ans += 1 
                maxp = i[1]
            else:
                maxp = min(maxp,i[1])
        ans += 1
        return ans