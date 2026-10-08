class Solution {
    public String removeOuterParentheses(String s) {
        StringBuilder ans=new StringBuilder();
        int c=0;
        for(char i:s.toCharArray()){
            if(i=='('){
                c+=1;
                if(c>1)ans.append(i);
            }
            else{
                c-=1;
                if(c>0)ans.append(i);
            }
        }
        return ans.toString();
    }
}