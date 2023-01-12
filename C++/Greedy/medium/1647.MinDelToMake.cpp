class Solution {
public:
    int minDeletions(string s) {
        
        unordered_map<char,int> hast;

        for(auto x : s){
            if(hast.find(x) != hast.end()){
                hast[x] +=1;
            }
            else{
                hast[x] = 1;
            }
        }

        set<int> v;
        int ans = 0;
        for(auto x : hast){
            int t = x.second;
            while(t > 0 && v.find(t) != v.end()){
                t = t-1;
                ans +=1;
            }
            v.insert(t);
        }

        return ans;

    }
};