class Solution {
public:
    int deleteAndEarn(vector<int>& nums) {
        
        vector<int> freq;
        
        for(int i = 0; i < (*max_element(nums.begin(),nums.end()))+1 ; i++){
            freq.push_back(0);
        }

        for(int i = 0; i < nums.size();i++){
            freq[nums[i]]++;
        }

        vector<int> dp;

        for(int i = 0; i < (*max_element(nums.begin(),nums.end()))+1 ; i++){
            dp.push_back(0);
        }

        dp[0] = freq[0];
        dp[1] = freq[1];
        for(int i = 2; i < (*max_element(nums.begin(),nums.end()))+1 ; i++){
            dp[i] = max(dp[i-1], dp[i-2] + freq[i]*i);
        }

        for(auto i = dp.begin(); i < dp.end() ; i++){
            cout << *i << endl;
        }

        return dp[(*max_element(nums.begin(),nums.end()))];
    }
};