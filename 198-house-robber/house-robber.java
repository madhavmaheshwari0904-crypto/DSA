class Solution {
    public static int solve(int[]dp,int idx,int[]nums){
        if(idx==0)return nums[idx];
        if(idx<0)return 0;
        if(dp[idx]!=-1)return dp[idx];
        int take=nums[idx]+solve(dp,idx-2,nums);
        int not=0+solve(dp,idx-1,nums);
        return dp[idx]=Math.max(take,not);
    }
    public int rob(int[] nums) {
        int[]dp=new int[nums.length];
        Arrays.fill(dp,-1);
        return solve(dp,nums.length-1,nums);
        }
}