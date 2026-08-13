class Solution {
    public int solve(int[][]dp,int m,int n,int[][]grid){
        if(m<0 || n<0)return Integer.MAX_VALUE;
        if(m==0 && n==0)return grid[0][0];
        if(dp[m][n]!=0)return dp[m][n];
        return dp[m][n]=grid[m][n]+Math.min(solve(dp,m-1,n,grid),solve(dp,m,n-1,grid));
    }
    public int minPathSum(int[][] grid) {
        int m=grid.length-1;
        int n=grid[0].length-1;
        int[][]dp=new int[m+1][n+1];
        return solve(dp,m,n,grid);
    }
}