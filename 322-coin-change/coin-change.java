class Solution {
    public int solve(int idx,int t,int[] coins,int[][]dp){
        if(idx==0){
            if((t%coins[idx])==0)return t/coins[idx];
            else return Integer.MAX_VALUE;
        }
        if(dp[idx][t]!=-1)return dp[idx][t];
        int not_take=0+solve(idx-1,t,coins,dp);
        int take=Integer.MAX_VALUE;
        if(coins[idx]<=t){
            int res=solve(idx,t-coins[idx],coins,dp);
            if(res!=Integer.MAX_VALUE)take=1+res;
        }
        return dp[idx][t]= Math.min(take,not_take);
    }
    public int coinChange(int[] coins, int amount) {
        int n=coins.length;
        int[][]dp=new int[n][amount+1];
        for(int[]r:dp)Arrays.fill(r,-1);
        int ans=solve(n-1,amount,coins,dp);
        return (ans==Integer.MAX_VALUE)?-1:ans;
    }
}