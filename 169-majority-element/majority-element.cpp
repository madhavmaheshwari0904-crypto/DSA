class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int can=nums[0];
        int c=1;
        for( int i=1;i<nums.size();i++){
            if(nums[i]!=can){
                if(c==0){
                    can=nums[i];
                    c++;
                }
                else{
                    c-=1;
                }
            }
            else{
                c++;
            }
        }
        return can;
    }
};