class Solution {
public:
    string minRemoveToMakeValid(string s) {
        vector<int> S;
        for(int i = 0; i < s.size();i++){
            if(s[i] == '('){
                S.push_back(i);
            }
            else if(s[i] == ')'){
                if(S.size() == 0){
                    s[i] = '#';
                }
                else{
                    S.pop_back();
                }
            }
            
        }
        string res = "";
        for(int i = 0; i < S.size();i++){
            s[S[i]] = '#';
        }
        for(int i =0; i < s.size();i++){
            if(s[i] != '#'){
                res.push_back(s[i]);
            }
        }

        return res;
    }
};