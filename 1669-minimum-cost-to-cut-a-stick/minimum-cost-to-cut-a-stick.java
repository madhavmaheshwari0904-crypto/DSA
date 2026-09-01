class Solution {
    public int minCost(int n, int[] cuts) {
        int m=cuts.length;
        int[]ans=new int[m+2];
        ans[0]=0;
        for(int i =0;i<m;i++){
            ans[i+1]=cuts[i];
        }
        ans[m+1]=n;
        int[][]dp=new int[m+2][m+2];
        for(int[]r:dp){
            Arrays.fill(r,-1);
        }
        Arrays.sort(ans);
        return solve(1,m,ans,dp);
    }
    public int solve(int i,int j,int[]ans,int[][]dp){
        if(i>j)return 0;
        if(dp[i][j]!=-1)return dp[i][j];
        int mimi=Integer.MAX_VALUE;
        for(int k=i;k<=j;k++){
            int cost = (ans[j + 1] - ans[i - 1]) 
                     + solve(i, k - 1, ans, dp) 
                     + solve(k + 1, j, ans, dp);
            mimi=Math.min(mimi,cost);
        }
        return dp[i][j]=mimi;
    }
}