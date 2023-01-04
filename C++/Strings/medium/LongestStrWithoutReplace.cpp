class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        set<char> st;
        int l,r;
        l=r=0;
        int ans = 0;
        while(r < s.size()){
            while(st.find(s[r]) != st.end()){
                ans = max(ans,r-l);
                st.erase(s[l]);
                l++;
            }
            
                st.insert(s[r]);
                r++;
            
        }
        ans = max(ans,r-l);
        return ans;
    }
};