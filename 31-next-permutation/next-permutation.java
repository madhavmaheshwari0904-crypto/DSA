class Solution {
    public void reverse(int[]nums,int i){
        int j=nums.length-1;
        while(i<j){
            int t=nums[i];
            nums[i]=nums[j];
            nums[j]=t;
            i++;
            j--;
        }
        return ;
    }
    public void nextPermutation(int[] nums) {
        int idx=-1;
        int n=nums.length;
        for(int i=n-2;i>=0;i--){
            if(nums[i]<nums[i+1]){
                idx=i;
                break;
            }
        }
        if(idx==-1){
            reverse(nums,0);
            return;
        }
        for(int i=n-1;i>idx;i--){
            if(nums[i]>nums[idx]){
                int t=nums[idx];
                nums[idx]=nums[i];
                nums[i]=t;
                break;
            }
        }
        reverse(nums,idx+1);
    }
}