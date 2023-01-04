class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> prefix;
        vector<int> suffix;
        int prod = 1;
        for(int i = 0; i < nums.size();i++ ){
            prod = prod*nums[i];
            prefix.push_back(prod);
        }

        for(int i = 0; i < nums.size();i++ ){
            suffix.push_back(0);
        }
        prod = 1;
        for(int i = nums.size() - 1; i >= 0;i-- ){
            prod = prod*nums[i];
            suffix[i] = prod;
        }

        vector<int> res;
        res.push_back(suffix[1]);
        for(int i = 1; i < nums.size() - 1;i++){
            res.push_back(prefix[i-1]*suffix[i+1]);
        }
        res.push_back(prefix[nums.size()-2]);

        return res;
    }
};