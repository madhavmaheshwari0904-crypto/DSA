class Solution {
    public int longestSubsequence(int[] nums) {
        int total=0;
        boolean flage=false;
        for(int i:nums){
            total^=i;
            if(i!=0)flage=true;
        }
        if(!flage)return 0;
        if(total!=0)return nums.length;
        return nums.length-1;
    }
}