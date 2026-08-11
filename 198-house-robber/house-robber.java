class Solution {
    //MEMORIZATION
    /*public static int solve(int[]dp,int idx,int[]nums){
        if(idx==0)return nums[idx];
        if(idx<0)return 0;
        if(dp[idx]!=-1)return dp[idx];
        int take=nums[idx]+solve(dp,idx-2,nums);
        int not=0+solve(dp,idx-1,nums);
        return dp[idx]=Math.max(take,not);
    }*/
    public int rob(int[] nums) {
        int prev=nums[0];
        int prev2=0;
        for(int i=0;i<nums.length;i++){
            int take=nums[i];
            if(i>1)take+=prev2;
            int not=0+prev;
            int curr=Math.max(take,not);
            prev2=prev;
            prev=curr;
        }
        return prev;
    }
}