class Solution {
    public int solve(int[] dp,int idx,int[]cost){
        if(idx<0)return 0;
        if (idx==0 || idx==1) return cost[idx];
        if(dp[idx]!=-1)return dp[idx];
        dp[idx]=cost[idx]+Math.min(solve(dp,idx-1,cost),solve(dp,idx-2,cost));
        return dp[idx];
    } 
    public int minCostClimbingStairs(int[] cost) {
        int []dp=new int[cost.length];
        Arrays.fill(dp,-1);
        dp[0]=cost[0];
        return Math.min(solve(dp,cost.length-1,cost),solve(dp,cost.length-2,cost));
    }
}