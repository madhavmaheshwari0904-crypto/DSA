class Solution {
    public int shortestPath(int[][] grid, int k) {
        int m = grid.length;
        int n = grid[0].length;
        int[]dx={1,-1,0,0};
        int[]dy={0,0,1,-1};
        if (k>=m+n-2)return m+n-2;
        Queue<int[]> queue = new ArrayDeque<>();
        queue.offer(new int[]{0, 0, k, 0});
        boolean[][][] vis = new boolean[m][n][k + 1];
        vis[0][0][k] = true;
        while(!queue.isEmpty()){
            int[]curr=queue.poll();
            int i=curr[0];
            int j=curr[1];
            int rem=curr[2];
            int step=curr[3];
            if (i==m-1 && j==n-1)return step;
            for(int l=0;l<4;l++){
                int ni=i+dx[l];
                int nj=j+dy[l];
                if(ni >= 0 && ni < m && nj >= 0 && nj < n){
                    int new_k=rem-grid[ni][nj];
                    if (new_k>=0 && vis[ni][nj][new_k]==false){
                        vis[ni][nj][new_k]=true;
                        queue.offer(new int[]{ni, nj, new_k, step+1});
                    }
                }
            }
        }
        return -1;
    }
}