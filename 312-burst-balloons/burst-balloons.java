class Solution {
    public int maxCoins(int[] nums) {
      int m=nums.length;
        int[]ans=new int[m+2];
        ans[0]=1;
        for(int i =0;i<m;i++){
            ans[i+1]=nums[i];
        }
        ans[m+1]=1;
        int[][]dp=new int[m+2][m+2];
        for(int[]r:dp){
            Arrays.fill(r,-1);
        }
        return solve(1,m,ans,dp);
    }
    public int solve(int i,int j,int[]ans,int[][]dp){
        if(i>j)return 0;
        if(dp[i][j]!=-1)return dp[i][j];
        int maxi=0;
        for(int k=i;k<=j;k++){
            int cost=(ans[i-1]*ans[k]*ans[j+1])+solve(i,k-1,ans,dp)+solve(k+1,j,ans,dp);
            maxi=Math.max(maxi,cost);
        }
        return dp[i][j]=maxi;
    }
}