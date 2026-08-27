class Solution {
    public int solve(int i,int[]prices,int buy,int[][]dp,int fee){
        if(i>=prices.length)return 0;
        if(dp[i][buy]!=-1)return dp[i][buy];
        if(buy==1){
            return dp[i][buy]= Math.max(-prices[i]+solve(i+1,prices,0,dp,fee),0+solve(i+1,prices,1,dp,fee));
        }
        else{
            return dp[i][buy]=Math.max(prices[i]-fee+solve(i+1,prices,1,dp,fee),0+solve(i+1,prices,0,dp,fee));
        }
        //return dp[i][buy]
    }
    public int maxProfit(int[] prices,int fee) {
        int n = prices.length;
        int[][]dp=new int[n][2];
        for (int[] row : dp) {
            Arrays.fill(row, -1);
        }
        return solve(0,prices,1,dp,fee);
    }
}