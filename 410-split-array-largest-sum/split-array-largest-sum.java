class Solution {
    public int splitArray(int[] nums, int k) {
        int low=0;
        int high=0,ans=0;
        for(int i=0;i<nums.length;i++){
            low=Math.max(low,nums[i]);
            high+=nums[i];
        }
        ans=low;
        while(low<=high){
            int mid=(low+high)/2;
            int s=0;
            int m=1;
            for(int i=0;i<nums.length;i++){
                if(s+nums[i]>mid){
                    m+=1;
                    s=nums[i];
                }
                else s+=nums[i];
            }
            if(m<=k){
                ans=mid;
                high=mid-1;
            }
            else low=mid+1;
        }
        return ans;
    }
}