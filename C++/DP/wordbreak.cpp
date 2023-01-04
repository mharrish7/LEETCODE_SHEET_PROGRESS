class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        int n = s.size();
        vector<int> dp;

        for(int i = 0; i < s.size() + 1;i++){
            dp.push_back(0);
        }

        dp[0] = 1;
        string st;
        for(int i = 0; i< s.size();i++){
            st += s[i];
            for(int j = 0; j < wordDict.size();j++){
                int t =  st.size()-wordDict[j].size();
                if(t >= 0){
                    string temp = st.substr(t,wordDict[j].size());
                    if(temp == wordDict[j]){
                        dp[i+1] = (dp[st.size() - wordDict[j].size()] || dp[i+1]);
                    }
                }
            }
        }
        return dp[s.size()];
    }
};