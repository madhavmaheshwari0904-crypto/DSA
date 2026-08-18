class Solution {
    //MEMORIZATION
    public boolean solve(int i,int sum,int[]nums,Boolean[][]dp){
        if(sum==0)return true;
        if(i==0)return (nums[i]==sum);
        if(dp[i][sum]!=null)return dp[i][sum];
        boolean not_take=solve(i-1,sum,nums,dp);
        boolean take=false;
        if(sum>=nums[i])take=solve(i-1,sum-nums[i],nums,dp);
        return dp[i][sum]= (take || not_take);
    }
    public boolean canPartition(int[] nums) {
        int s=0;
        for(int i:nums){
            s+=i;
        }
        if(s%2==1)return false;
        int target = s / 2;
        int n = nums.length;
        boolean[][] dp = new boolean[n][target + 1];
        for(int i=0;i<n;i++)dp[i][0]=true;
        if (nums[0] <= target) {
            dp[0][nums[0]] = true;
        }
        for(int idx=1;idx<n;idx++){
            for(int t=1;t<=target;t++){
                boolean not_take=dp[idx-1][t];
                boolean take=false;
                if(t>=nums[idx])take=dp[idx-1][t-nums[idx]];
                dp[idx][t]= (take || not_take);
                }
            }
        return dp[n-1][target];
    }
}