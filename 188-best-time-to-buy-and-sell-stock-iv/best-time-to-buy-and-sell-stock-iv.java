class Solution {
    public int solve(int i,int[] prices,int k,int buy,int[][][]dp){
        if(i==prices.length)return 0;
        if(k==0)return 0;
        if(dp[i][buy][k]!=-1)return dp[i][buy][k];
        int pro=0;
        if(buy==1) {
            pro= Math.max(-prices[i]+solve(i+1,prices,k,0,dp),0+solve(i+1,prices,k,1,dp));
        }
        else{
            pro= Math.max(prices[i]+solve(i+1,prices,k-1,1,dp),0+solve(i+1,prices,k,0,dp));
        }
        return dp[i][buy][k]=pro;
    }
    public int maxProfit(int k, int[] prices) {
       int[][][]dp=new int[prices.length][2][k+1];
       for(int i=0;i<prices.length;i++){
        for(int j=0;j<2;j++){
            Arrays.fill(dp[i][j],-1);
        }
       }
       return solve(0,prices,k,1,dp);
    }
}