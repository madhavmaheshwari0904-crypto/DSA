class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        int n=nums.length;
        Arrays.sort(nums);
        List<List<Integer>> ans=new ArrayList<>();
        if (nums == null || nums.length < 4) return ans;
        for(int i=0;i<n-3;i++){
            if(i>0 && nums[i]==nums[i-1])continue;
            for(int j=i+1;j<n-2;j++){
                if(j>i+1 && nums[j]==nums[j-1])continue;
                int k=j+1;
                int l=n-1;
                while(k<l){
                    long s=(long)nums[i]+nums[j]+nums[k]+nums[l];
                    if(s==target){
                        ArrayList<Integer>curr=new ArrayList<>();
                        curr.add(nums[i]);
                        curr.add(nums[j]);
                        curr.add(nums[k]);
                        curr.add(nums[l]);
                        ans.add(curr);
                        k+=1;
                        l-=1;
                        while(k<l && nums[k]==nums[k-1])k+=1;
                        while(k<l && nums[l]==nums[l+1])l-=1;
                    }
                    else if(s<target){
                        k+=1;
                    }
                    else l-=1;
                }
            }
        }
        return ans;
    }
}