class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        stack = []
        for i in num:
            i1 = int(i)
            while stack and stack[-1] > i1 and k > 0:
                stack.pop()
                k-=1
            stack.append(i1)
        
        res = ""
        while k and stack:
            stack.pop()
            k -=1 

        while stack and stack[0] == 0:
            stack.pop(0)
        for i in stack:
            res += str(i)
        if not stack:
            return "0"
        return res