class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        prevs = intervals[0][0]
        preve = intervals[0][1]
        R = []
        for i in range(1,len(intervals)):
            if intervals[i][0] <= preve:
                preve = max(intervals[i][1],preve)
            else:
                R.append([prevs,preve])
                prevs = intervals[i][0]
                preve = intervals[i][1]
        R.append([prevs,preve])
        return R

