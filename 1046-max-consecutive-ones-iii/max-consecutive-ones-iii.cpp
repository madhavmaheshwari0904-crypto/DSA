class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int m=0;
        int i=0,j=0;
        while(j< nums.size()){
            if(nums[j]==0){
                k--;
            }
            j++;
            if(k<0){
                if(nums[i]==0){
                    k+=1;
                }
                i+=1;
            }
        }
        return j-i;
    }

};