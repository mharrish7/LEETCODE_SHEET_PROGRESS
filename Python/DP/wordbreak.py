class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False]*(len(s) + 1)
        dp[0] = True 
        st = ""
        for i in range(len(s)):
            st += s[i] 
            for j in wordDict:
                if len(st) - len(j) + 1 >= 0:
                    if st[len(st)- len(j):] == j: 
                        dp[i+1] = (dp[len(st)-len(j)] or dp[i+1])

        print(dp)
        return dp[-1] 