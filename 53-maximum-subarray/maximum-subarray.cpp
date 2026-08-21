class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        /*int m=-10001;
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
        }*/
        int m=nums[0];
        int curr=nums[0];
        for(int i=1;i<nums.size();i++){
            curr=curr+nums[i];
            curr=max(curr,nums[i]);
            m=max(m,curr);
        }
        return m;
    }
};