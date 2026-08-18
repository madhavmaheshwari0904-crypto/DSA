class Solution {
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
        else{
            int n=nums.length;
            Boolean[][]dp=new Boolean[n][s/2+1];
            return solve(n-1,s/2,nums,dp);
        }
    }
}