class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:

        hast = {}
        for i,j in zip(edges,hasApple):
            if i[0] in hast:
                hast[i[0]].append(i[1])
            else:
                hast[i[0]] = [i[1]]
            
            if i[1] in hast:
                hast[i[1]].append(i[0])
            else:
                hast[i[1]] = [i[0]]
        visited = set()
        def rec(root):

            if root in visited:
                return -1 
            visited.add(root)
            if hasApple[root]:
                ans = 0 
                if root in hast:
                    for i in hast[root]:
                        a = rec(i)
                        if a != -1:
                            ans += a 
                return 2 + ans

            if root not in hast:
                return -1 
            
            ans = 0 
            for i in hast[root]:
                a = rec(i)
                if a != -1:
                    ans += a 
            if ans == 0:
                return -1 
            else:
                return ans + 2  
        
        ans = rec(0)
        if ans == -1:
            return 0 
        return ans-2
        