class Solution {
    public int solve(String  text,int left ,int right){
        if(left>right)return 0;
        for(int l=1;l<=(right-left+1)/2;l++){
            boolean match = true;
            for (int i = 0; i < l; i++) {
                if (text.charAt(left + i) !=
                    text.charAt(right - l + 1 + i)) {
                    match = false;
                    break;
                }
            }
            if (match) {
                return 2 + solve(text,
                                 left + l,
                                 right - l);
            }
        }
        return 1;
    }
    public int longestDecomposition(String text) {
        /*int n=text.length();
        for(int i=0;i<n/2;i++){
            if(text.substring(0,i+1).equals(text.substring(n-i-1,n)))
            return 2+longestDecomposition(text.substring(i+1,n-i-1));
        }
        return (n==0)?0:1;*/
        return solve(text,0,text.length()-1);
    }
}