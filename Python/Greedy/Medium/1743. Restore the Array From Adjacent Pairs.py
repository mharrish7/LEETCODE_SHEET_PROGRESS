class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        hast = {}
        for i in adjacentPairs:
            if i[0] in hast:
                hast[i[0]].append(i[1])
            else:
                hast[i[0]] = [i[1]]
            
            if i[1] in hast:
                hast[i[1]].append(i[0])
            else:
                hast[i[1]] = [i[0]]

        a,b = 0,0
        for i in hast:
            if len(hast[i]) == 1:
                if a:
                    b = i 
                else:
                    a = i
        visited = set()
        
        R = [a]
        Q = [a]
        while len(Q) > 0:
            t = Q.pop(0)
            visited.add(t)
            for i in hast[t]:
                if i not in visited:
                    Q.append(i)
                    R.append(i)
        
        return R