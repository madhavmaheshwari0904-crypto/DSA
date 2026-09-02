class Solution {
    public int solve(int i,int[]arr,int k,int[]dp){
        if(i==arr.length)return 0;
        if(dp[i]!=-1)return dp[i];
        int l=0;
        int ans=Integer.MIN_VALUE;
        int maxi=Integer.MIN_VALUE;
        for(int j=i;j<Math.min(i+k,arr.length);j++){
            l++;
            maxi=Math.max(maxi,arr[j]);
            int cost=l*maxi+solve(j+1,arr,k,dp);
            ans=Math.max(ans,cost);
        }
        return dp[i]=ans;
    }
    public int maxSumAfterPartitioning(int[] arr, int k) {
        int[]dp=new int[arr.length];
        Arrays.fill(dp,-1);
        return solve(0,arr,k,dp);
    }
}