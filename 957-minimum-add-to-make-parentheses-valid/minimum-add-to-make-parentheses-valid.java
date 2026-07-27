class Solution {
    public int minAddToMakeValid(String s) {
        int open=0;
        int mis=0;
        for(char i:s.toCharArray()){
            if(i=='(')open+=1;
            else{
                if(open>0)open-=1;
                else mis+=1;
            }
        }
        return mis+open;
    }
}