class Solution {
    public int numberOfSubarrays(int[] nums, int k) {
        int l=0,r=0;
        int odd=0,c=0,t=0;
        while(r<nums.length){
            if(nums[r]%2==1){
                odd++;
                t=0;
            }
            while(odd==k){
                t++;
                if(nums[l]%2==1){
                    odd--;
                }
                l++;
            }
            c+=t;
            r++;
        }
        return c;
    }
}