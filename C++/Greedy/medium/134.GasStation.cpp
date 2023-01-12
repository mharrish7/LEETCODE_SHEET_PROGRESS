class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int sum1 =0; 
        sum1 = accumulate(gas.begin(),gas.end(),sum1);
        int sum2 =0; 
        sum2 = accumulate(cost.begin(),cost.end(),sum2);
        if(sum2 > sum1){
            return -1;
        }

        vector<int> dif;
        for(int i = 0; i < gas.size();i++){
            dif.push_back(gas[i]-cost[i]);
        }

        int ans = 0; 
        int t = 0;
        for(int i = 0; i < gas.size();i++){
            if(t < 0){
                t = 0;
                ans = i;
            }
            t = t + dif[i];

        }
        return ans;

    }
};