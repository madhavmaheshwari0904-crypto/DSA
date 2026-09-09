class Solution {
    int mod=1000000000 + 7;
    public int solve(int n,int goal,int k,int[][]dp){
        if(n==0 && goal==0)return 1;
        if(n==0 || goal==0)return 0;
        if(dp[n][goal]!=-1)return dp[n][goal];
        long take = (solve(n - 1, goal - 1, k, dp) * (long) n) % mod;
        long not_take = (solve(n, goal - 1, k, dp) * (long) Math.max(n - k, 0)) % mod;
        return dp[n][goal] = (int) ((take + not_take) % mod);
    }
    public int numMusicPlaylists(int n, int goal, int k) {
        int[][]dp=new int[n+1][goal+1];
        for(int[]r:dp){
            Arrays.fill(r,-1);
        }
        return (int)solve(n,goal,k,dp);
    }
}