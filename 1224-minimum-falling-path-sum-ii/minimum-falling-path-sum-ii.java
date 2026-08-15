class Solution {
    public int minFallingPathSum(int[][] matrix) {
        int n = matrix.length;
        int[] dp = matrix[n-1].clone();
        for (int r = n-2; r >= 0; r--) {
            int min1 = Integer.MAX_VALUE, min2 = Integer.MAX_VALUE;
            for (int val : dp) {
                if (val <= min1) {
                    min2 = min1;
                    min1 = val;
                } else if (val < min2) {
                    min2 = val;
                }
            }
        int[] newDp = new int[n];
            for (int c = 0; c < n; c++) {
                newDp[c] = (dp[c] == min1) ? matrix[r][c] + min2 : matrix[r][c] + min1;
            }
            dp = newDp;
        }
        int ans = Integer.MAX_VALUE;
        for (int val : dp) ans = Math.min(ans, val);
        return ans;
    }
}