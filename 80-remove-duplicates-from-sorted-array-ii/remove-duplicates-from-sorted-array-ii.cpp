class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if(nums.size()==1){
            return 1;
        }
        int c=2;
        for(int j=2;j<nums.size();j++){
            if(nums[c-2]!=nums[j]){
                nums[c]=nums[j];
                c++;
            }
        }
        return c;
    }
};