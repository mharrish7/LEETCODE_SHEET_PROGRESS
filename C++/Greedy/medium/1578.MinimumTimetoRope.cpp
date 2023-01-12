class Solution {
public:
    int minCost(string colors, vector<int>& neededTime) {
        int ans = 0;
        int sums = neededTime[0];
        int maxs = neededTime[0];
        for(int i = 1; i < colors.size();i++){
            if(colors[i] == colors[i-1]){
                sums += neededTime[i];
                maxs = max(maxs,neededTime[i]);
            }
            else{
                ans += (sums - maxs);
                sums = neededTime[i];
                maxs = neededTime[i];
            }
        }
        ans += (sums - maxs);
        return ans;
    }
};