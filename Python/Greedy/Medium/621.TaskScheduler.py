class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        WaitQ = []
        hast = {}
        for i in tasks:
            if i in hast:
                hast[i]+=1 
            else:
                hast[i] = 1 
        
        L = []
        for i in hast:
            L.append([-hast[i],i])
        heapq.heapify(L)
        time = 1
        while len(L) > 0 or len(WaitQ) > 0:
            while len(WaitQ) > 0 and WaitQ[0][1] <= time:
                t = WaitQ.pop(0)
                heapq.heappush(L,t[0])
            if len(L) > 0:
                t1 = heapq.heappop(L)
                t1[0] = t1[0] + 1
                if -t1[0] > 0:
                    WaitQ.append([t1,time+n+1])
            time += 1 
        return time - 1


