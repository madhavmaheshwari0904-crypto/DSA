class Solution {
    public boolean solve(String w1,String w2){
        int i = 0, j = 0;
        while (i < w1.length() && j < w2.length()) {
            if (w1.charAt(i) == w2.charAt(j)) {
                i++;
            }
            j++;
        }
        return i == w1.length();
    }
    public int longestStrChain(String[] words) {
        if (words == null || words.length == 0) return 0;
        int n=words.length;
        int[] dp=new int[n];
        Arrays.fill(dp,1);
        int maxi=1;
        Arrays.sort(words,Comparator.comparingInt(String::length));
        for(int i=1;i<n;i++){
            for(int j=0;j<i;j++){
                if (words[i].length() - words[j].length() == 1 && solve(words[j], words[i]) && dp[j]+1>dp[i])dp[i]=dp[j]+1;
            }
            if(dp[i]>maxi)maxi=dp[i];
        }
        return maxi;
    }
}