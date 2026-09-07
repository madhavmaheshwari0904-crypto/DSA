class Solution {
    public int solve(int i,int j,int[][]dp){
        if(i>=j)return 0;
        if(dp[i][j]!=-1)return dp[i][j];
        int maxi=Integer.MAX_VALUE;
        for(int k=i;k<=j;k++){
            maxi=Math.min(maxi,Math.max(k+solve(i,k-1,dp),k+solve(k+1,j,dp)));
        }
        return dp[i][j]=maxi;
    }
    public int getMoneyAmount(int n) {
        int[][]dp=new int[n+1][n+1];
        for(int[] i:dp){
            Arrays.fill(i,-1);
        }
        return solve(1,n,dp);
    }
}