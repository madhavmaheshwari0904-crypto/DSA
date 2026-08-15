class Solution {
    /*public int solve(int i,int j,int m,int n,int[][]matrix,int[][] dp){
        if (j < 0 || j >= n) return (int) 1e9;
        if (i == 0) return matrix[0][j];
        if (dp[i][j] != -1) return dp[i][j];
        int straight = matrix[i][j] + solve(i - 1, j, m, n, matrix, dp);
        int leftDiag  = matrix[i][j] + solve(i - 1, j - 1, m, n, matrix, dp);
        int rightDiag = matrix[i][j] + solve(i - 1, j + 1, m, n, matrix, dp);
        return dp[i][j] = Math.min(straight, Math.min(leftDiag, rightDiag));
    }*/
    public int minFallingPathSum(int[][] matrix) {
        int n = matrix.length;

    for (int i = 1; i < n; i++) {
        for (int j = 0; j < n; j++) {
            int straight  = matrix[i - 1][j];
            int leftDiag  = (j > 0) ? matrix[i - 1][j - 1] : (int) 1e9;
            int rightDiag = (j < n - 1) ? matrix[i - 1][j + 1] : (int) 1e9;

            matrix[i][j] += Math.min(straight, Math.min(leftDiag, rightDiag));
        }
    }
    int minSum = Integer.MAX_VALUE;
    for (int val : matrix[n - 1]) {
        minSum = Math.min(minSum, val);
    }
    return minSum;
    }
}