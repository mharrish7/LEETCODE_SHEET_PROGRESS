class Solution {
public:
    string longestPalindrome(string s) {
     int l,r;
     int res = 0;
     string ress = "";

     for(int i = 0; i < s.size();i++){
         l=r=i;
         while(l >=0 && r < s.size() && s[l] == s[r]){
             if(r-l+1 > res){
                res = r-l+1;
                ress = s.substr(l,r-l+1);
             }
             l-=1;
             r+=1;
         }
         
     }
     for(int i = 0; i < s.size();i++){
         l=i;
         r=i+1;
         while(l >=0 && r < s.size() && s[l] == s[r]){
             if(r-l+1 > res){
                res = r-l+1;
                ress = s.substr(l,r-l+1);
             }
             l-=1 ;
             r+=1;
         }
     }

     return ress;
    }
};