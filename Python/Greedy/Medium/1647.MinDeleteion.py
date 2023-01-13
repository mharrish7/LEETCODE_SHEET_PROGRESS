class Solution:
    def minDeletions(self, s: str) -> int:

        hast = {}
        for i in s:
            if i in hast:
                hast[i]+=1 
            else:
                hast[i] = 1 
        v = set()
        ans = 0
        for i in hast:
            while hast[i] > 0 and hast[i] in v:
                hast[i] -=1 
                ans += 1 
            
            v.add(hast[i])
        return ans

                    