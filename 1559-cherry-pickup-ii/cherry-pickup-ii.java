class Solution {
    //FOR MEMORIZATION TC=(N*M*M)
    public int solve(int i,int j1,int j2,int[][]grid,Integer[][][]dp ){
        int m = grid[0].length;
        if(j1<0 || j1>=m || j2<0 || j2>=m)return (int) -1e8;
        if(i==grid.length-1){
            if(j1==j2)return grid[i][j1];
            else return grid[i][j1]+grid[i][j2];
        }
        if (dp[i][j1][j2] != null) return dp[i][j1][j2];
        int maxi=(int) -1e8;;
        for(int k=-1;k<2;k++){
            for(int l=-1;l<2;l++){
                int cherries = (j1 == j2) ? grid[i][j1] : grid[i][j1] + grid[i][j2];
                cherries += solve(i + 1, j1 + k, j2 + l, grid, dp); 
                maxi = Math.max(maxi, cherries);
            }
        }
        return dp[i][j1][j2] = maxi; 
    }
    //TLE because TC=(3^n*3^n)  for RECURSION
    public int cherryPickup(int[][] grid) {
        int n = grid.length, m = grid[0].length;
        Integer[][][] dp = new Integer[n][m][m];
        return solve(0,0,m-1,grid,dp);
    }
}