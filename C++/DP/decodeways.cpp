class Solution {
public:
    int numDecodings(string s) {
        
        vector<int> dp;
        for(int i = 0; i < s.size() +1; i++){
            dp.push_back(0);
        }
        dp[s.size()] = 1;

        for(int i = s.size()-1; i >= 0; i--){
            if(s[i] == '0'){
                dp[i] = 0;
                cout << 7 << 1;
            }
            else{
                dp[i] = dp[i+1];
            }

            if((i+1 < s.size() and s[i] == '1') or (s[i] == '2' and i+1 < s.size() and (s[i+1] == '0' or s[i+1] == '1' or s[i+1] == '2' or s[i+1] == '3' or s[i+1] == '4' or s[i+1] == '5' or s[i+1] == '6'))){
                dp[i] = dp[i] + dp[i+2];
                cout << 8;

            }
        }

        for(int i = 0; i < s.size() +1; i++){
            cout << dp[i] << endl;
        }

        return dp[0]; 
    }
};