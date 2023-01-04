class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        S = []
        s = list(s)
        for i in range(len(s)):
            if s[i] == '(':
                S.append(i)
            elif s[i] == ')':
                if len(S) == 0:
                    s[i] = ""
                else:
                    S.pop()
        for i in S:
            s[i] = ""
        return "".join(s)