class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> R;
        for(int i = 0; i < nums.size()-2 ; i++){
            if( i > 0 && nums[i] == nums[i-1]){
                continue;
            }
            int l,r;
            l = i + 1;
            r = nums.size()-1;
            while(l < r){
                if(nums[i] + nums[l] + nums[r] == 0){
                    R.push_back({nums[i], nums[l] , nums[r]});
                    l++;
                    r--;
                    while(l < r && nums[l] == nums[l-1]){
                        l++;
                    }
                }
                else if(nums[i] + nums[l] + nums[r] < 0){
                    l++;
                }
                else{
                    r--;
                }
            }
        }

        return R;
    }
};