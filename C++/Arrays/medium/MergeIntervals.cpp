class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        
        vector<vector<int>> R;
        

        sort(intervals.begin(), intervals.end());

        int prevs = intervals[0][0];
        int preve = intervals[0][1];
        
        for(int i = 0 ; i < intervals.size(); i++){
            if(intervals[i][0] <= preve){
                preve = max(intervals[i][1], preve);
            }
            else{
                R.push_back({prevs,preve});
                preve = intervals[i][1];
                prevs = intervals[i][0];
            }
        }
        R.push_back({prevs,preve});
        return R;
    }
};