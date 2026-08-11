class Solution {
    public int solve(List<Integer>dp) {
        int n=dp.size();
        if (n == 0) return 0;
        int prev=dp.get(0);
        int prev2=0;
        for(int i=0;i<n;i++){
            int take=dp.get(i);
            if(i>1)take+=prev2;
            int not=0+prev;
            int curr=Math.max(take,not);
            prev2=prev;
            prev=curr;
        }
        return prev;
    }
    public int rob(int[] nums) {
        List<Integer>temp1=new ArrayList<>();
        List<Integer>temp2=new ArrayList<>();
        int n=nums.length;
        if (n == 1) return nums[0];
        for(int i=0;i<n;i++){
            if(i!=0)temp1.add(nums[i]);
            if(i!=n-1)temp2.add(nums[i]);
        }
        return Math.max(solve(temp1),solve(temp2));
    }
}