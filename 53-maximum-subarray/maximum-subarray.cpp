class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int m=-10001;
        int l=0;
        int r=0;
        int curr=0;
        while(r<nums.size()){
            curr=curr+nums[r];
            m=max(m,curr);
            if(curr<0){
                curr=0;
                l++;
            }
            r++;
        }
        return m;
    }
};