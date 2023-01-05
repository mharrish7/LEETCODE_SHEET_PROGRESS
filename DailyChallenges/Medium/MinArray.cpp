class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        sort(points.begin(),points.end());
        int maxp = points[0][1];
        int ans = 0;
        for(int i=1; i<points.size();i++){
            if(maxp < points[i][0]){
                ans+=1 ;
                maxp = points[i][1];
            }
            else{
                maxp = min(maxp,points[i][1]);
            }
        }
        return ans+1;
    }
};