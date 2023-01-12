class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        sums = neededTime[0]
        maxs = neededTime[0]
        for i in range(1,len(colors)):
            if colors[i] == colors[i-1]:
                sums += neededTime[i]
                maxs = max(neededTime[i],maxs)
            else:
                ans += sums - maxs
                sums = neededTime[i]
                maxs = neededTime[i]
        ans += sums - maxs

        return ans
            