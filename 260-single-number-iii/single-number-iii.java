class Solution {
    public int[] singleNumber(int[] nums) {
        int n1=0,n2=0;
        int ans=0;
        for(int i:nums){
            ans^=i;
        }
        int diff=(ans & ans-1)^ans;
        for(int i:nums){
            if ((i & diff)!=0)n1^=i;
            else n2^=i;
        }
        return new int[]{n1,n2};
    }
}