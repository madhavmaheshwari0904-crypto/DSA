class Solution {
    public int solve(int i,int j,int[][] matrix,int[][]dp){
        if(dp[i][j]>0)return dp[i][j];
        int val=matrix[i][j];
        int down=(i<matrix.length-1 && matrix[i+1][j]<val)?solve(i+1,j,matrix,dp):0;
        int up=(i>0 && matrix[i-1][j]<val)?solve(i-1,j,matrix,dp):0;
        int left=(j>0 && matrix[i][j-1]<val)?solve(i,j-1,matrix,dp):0;
        int right=(j<matrix[0].length-1 && matrix[i][j+1]<val)?solve(i,j+1,matrix,dp):0;
        dp[i][j]=1+Math.max(Math.max(down, up), Math.max(right, left));
        return dp[i][j];
    }
    public int longestIncreasingPath(int[][] matrix) {
        int m=matrix.length;
        int n=matrix[0].length;
        int ans=0;
        int [][]dp=new int[m][n];
        for( int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                ans=Math.max(ans,solve(i,j,matrix,dp));
            }
        }
        return ans;
    }
}