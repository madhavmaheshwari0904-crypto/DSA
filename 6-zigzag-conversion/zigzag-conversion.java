class Solution {
    public String convert(String s, int numRows) {
        if(numRows==1 || numRows>=s.length())return s;
        int cycle=2*numRows-2;
        int n = s.length();
        StringBuilder ans =new StringBuilder();
        for(int r=0;r<numRows;r++){
            for(int i=0;i<n-r;i+=cycle){
                ans.append(s.charAt(r+i));
                int diag_index=i+cycle-r;
                if(r!=0 && r!=numRows-1 && diag_index<n)ans.append(s.charAt(diag_index));
            }
        }
        return ans.toString();
    }
}