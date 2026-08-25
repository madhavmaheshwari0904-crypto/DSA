class Solution {
    /*public int solve(int i,int j,String word1, String word2){
        if(i<0)return j+1;
        if(j<0)return i+1;
        if(word1.charAt(i)==word2.charAt(j))return solve(i-1,j-1,word1,word2);
        return 1+Math.min(solve(i-1,j,word1,word2),Math.min(solve(i,j-1,word1,word2),solve(i-1,j-1,word1,word2)));
    }*/
    public int solve(int i,int j,String word1, String word2,int[][]dp){
        if(i<0)return j+1;
        if(j<0)return i+1;
        if(dp[i][j]!=-1)return dp[i][j];
        if(word1.charAt(i)==word2.charAt(j)) return solve(i-1,j-1,word1,word2,dp);
        return dp[i][j]=1+Math.min(solve(i-1,j,word1,word2,dp),Math.min(solve(i,j-1,word1,word2,dp),solve(i-1,j-1,word1,word2,dp)));
    }
    public int minDistance(String word1, String word2) {
        int n=word1.length();
        int m=word2.length();
        int[][]dp=new int[n][m];
        for(int[]r:dp)Arrays.fill(r,-1);
        return solve(n-1,m-1,word1,word2,dp);
    }
}