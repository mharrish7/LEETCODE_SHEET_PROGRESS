class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:

        hast = {}
        for i in edges:
            if i[0] in hast:
                hast[i[0]].append(i[1])
            else:
                hast[i[0]] = [i[1]]
            if i[1] in hast:
                hast[i[1]].append(i[0])
            else:
                hast[i[1]] = [i[0]]
        ans = [0]*n
        labelc = {}
        for i in labels:
            labelc[i] = 0
        visited = set()
        def rec(root):
            if root not in hast:
                return 
            if root in visited:
                return 
            visited.add(root)
            prev = labelc[labels[root]]
            labelc[labels[root]] += 1 

            for i in hast[root]:
                rec(i)
            
            if prev == None:
                ans[root] = labelc[labels[root]]
            else:
                ans[root] = labelc[labels[root]] - prev
        rec(0)
        print(labelc)
        return ans