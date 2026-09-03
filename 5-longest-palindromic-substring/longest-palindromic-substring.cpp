class Solution {
public:
    bool pal(string &s,int i,int j){
        while(i<j){
            if(s[i]!=s[j])return false;
            i++;
            j--;
        }
        return true;
    }
    string longestPalindrome(string s) {
        int m=0,new_ind=0;
        for(int i =0;i<s.size();i++){
            for(int j=i;j<s.size();j++){
                if((j-i+1)>m && pal(s,i,j)==true){
                    m=j-i+1;
                    new_ind=i;
                }
            }
        }
        return s.substr(new_ind,m);
    }
};