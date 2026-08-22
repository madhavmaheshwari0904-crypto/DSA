class Solution {
    public int solve(int idx,int t,int[] coins,int[][]dp){
        if(idx==0){
            return (t % coins[0] == 0) ? 1 :0 ;
        }
        if(dp[idx][t]!=-1)return dp[idx][t];
        int not_take=0+solve(idx-1,t,coins,dp);
        int take=0;
        if(coins[idx]<=t){
            take=solve(idx,t-coins[idx],coins,dp);
        }
        return dp[idx][t]=(take+not_take);
    }
    public int change(int amount, int[] coins) {
        int n=coins.length;
        int[][]dp=new int[n][amount+1];
        for(int[]r:dp)Arrays.fill(r,-1);
        return solve(n-1,amount,coins,dp);
    }
}