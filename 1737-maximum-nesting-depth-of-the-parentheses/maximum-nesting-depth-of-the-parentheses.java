class Solution {
    public int maxDepth(String s) {
        int i=0;
        int m=0;
        int c=0;
        while(i<s.length()){
            if(s.charAt(i)=='('){
                c+=1;
                if(m<c)m=c;
            }
            if(s.charAt(i)==')')c-=1;
            i++;
        }
        return m;
    }
}