class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int l=0;
        int n=nums.size();
        int h=n-1;
        /*if(n<(k%n)){
            return;
        }*/
        while(l<h){
            nums[l]=nums[l]^nums[h];
            nums[h]=nums[l]^nums[h];
            nums[l]=nums[l]^nums[h];
            l++;
            h--;
        }
        l=0;
        h=(k%n)-1;
        while(l<h){
            nums[l]=nums[l]^nums[h];
            nums[h]=nums[l]^nums[h];
            nums[l]=nums[l]^nums[h];
            l++;
            h--;
        }
        l=k%n;
        h=nums.size()-1;
        while(l<h){
            nums[l]=nums[l]^nums[h];
            nums[h]=nums[l]^nums[h];
            nums[l]=nums[l]^nums[h];
            l++;
            h--;
        }
        return;
    }
};