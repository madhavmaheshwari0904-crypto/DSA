class Solution {
    public int maxSubarraySumCircular(int[] nums) {
        int n=nums.length;
        int t=0;
        int m1=0;
        int m2=nums[0];
        int mx1=0;
        int mx2=nums[0];
        for(int i:nums){
            t+=i;
            mx1=Math.max(mx1+i,i);
            mx2=Math.max(mx1,mx2);
            m1=Math.min(m1+i,i);
            m2=Math.min(m1,m2);
        }
        if(mx2<0)return mx2;
        return Math.max(t-m2,mx2);
    }
}