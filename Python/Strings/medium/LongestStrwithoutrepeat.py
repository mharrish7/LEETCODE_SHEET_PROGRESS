class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0
        st = set()
        ans = 0
        while r < len(s):
            if s[r] in st:
                ans = max(ans, r-l)
                st.remove(s[l])
                l+=1 
            else:
                st.add(s[r])
                r+=1 
        ans = max(ans,r-l)
        return ans