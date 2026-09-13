class Solution {
    public int solve(int n,int[]dp){
        if(n==0)return 0;
        if(dp[n]!=-1)return dp[n];
        int mini=Integer.MAX_VALUE;
        for(int i=1;i*i<=n;i++){
            int per=i*i;
            int ans=1+solve(n-per,dp);
            mini=Math.min(mini,ans);
        }
        dp[n]=mini;
        return dp[n];
    }
    public int numSquares(int n) {
        int[]dp=new int[n+1];
        Arrays.fill(dp,-1);
        return solve(n,dp);
    }
}