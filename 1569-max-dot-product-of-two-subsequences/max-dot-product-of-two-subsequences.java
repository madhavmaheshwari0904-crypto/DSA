class Solution {
    int n;
    int m;
    public int solve(int i,int j,int[]nums1,int[]nums2,int[][]dp){
        if(i==m || j==n)return (int)-1e9;
        if(dp[i][j]!=-1)return dp[i][j];
        int take=nums1[i]*nums2[j];
        int both=take+Math.max(0,solve(i+1,j+1,nums1,nums2,dp));
        int skip1=solve(i+1,j,nums1,nums2,dp);
        int skip2=solve(i,j+1,nums1,nums2,dp);
        int ans=Math.max(both,Math.max(skip1,skip2));
        return dp[i][j]=ans;
    }
    public int maxDotProduct(int[] nums1, int[] nums2) {
        m=nums1.length;
        n=nums2.length;
        int[][]dp=new int[m][n];
        for(int[]r:dp)Arrays.fill(r,-1);
        return solve(0,0,nums1,nums2,dp);
    }
}