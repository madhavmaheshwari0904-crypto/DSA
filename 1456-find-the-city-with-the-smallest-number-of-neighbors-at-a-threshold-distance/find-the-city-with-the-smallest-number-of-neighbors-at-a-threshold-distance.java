public class Solution {
    public int findTheCity(int n, int[][] edges, int distanceThreshold) {
        int[][] matrix = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                matrix[i][j] = Integer.MAX_VALUE;
            }
            matrix[i][i] = 0;
        }
        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];
            int wt = edge[2];
            matrix[u][v] = wt;
            matrix[v][u] = wt;
        }
        for (int via = 0; via < n; via++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (matrix[i][via] == Integer.MAX_VALUE || matrix[via][j] == Integer.MAX_VALUE) {
                        continue;
                    }
                    matrix[i][j] = Math.min(matrix[i][j], matrix[i][via] + matrix[via][j]);
                }
            }
        }
        int cntcity = n;
        int cityno = -1;

        for (int i = 0; i < n; i++) {
            int count = 0;
            for (int j = 0; j < n; j++) {
                if (i != j && matrix[i][j] <= distanceThreshold) {
                    count++;
                }
            }
            if (count <= cntcity) {
                cntcity = count;
                cityno = i;
            }
        }
        return cityno;
    }
}