class Solution {
    public int smallestDivisor(int[] nums, int threshold) {
        int low=1;
        int high=Integer.MIN_VALUE;
        int ans=high;
        for(int i:nums){
            high=Math.max(high,i);
        }
        while(low<=high){
            int mid=(low+high)/2;
            int s=0;
            for(int i: nums){
                s+=(i+mid-1)/mid;
            }
            if(s<=threshold){
                ans=mid;
                high=mid-1;
            }
            else{
                low=mid+1;
            }
        }
        return ans;    
    }
}