class Solution {
    public int solve(int i,int j,String s,int[][]dp){
        if(j<i)return 0;
        if(dp[i][j]!=-1)return dp[i][j];
        if(s.charAt(i)==s.charAt(j)){
            if(i==j)return dp[i][j]=1+solve(i+1,j-1,s,dp);
            else  return dp[i][j]=2+solve(i+1,j-1,s,dp);
        }
        return dp[i][j]=Math.max(solve(i+1,j,s,dp),solve(i,j-1,s,dp));
    }
    public int minInsertions(String s) {
        int i=0;
        int n=s.length();
        int j=n-1;
        int[][] dp=new int[n][n];
        for(int[]r:dp)Arrays.fill(r,-1);
        int ans= solve(i,j,s,dp);
        return n-ans;
    }
}