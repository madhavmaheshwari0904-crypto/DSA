class Solution {
    public int subarraySum(int[] nums, int k) {
        HashMap<Integer, Integer> ans = new HashMap<>();
        int pre=0;
        ans.put(0,1);
        int c=0;
        for(int i=0;i<nums.length;i++){
            pre+=nums[i];
            int r=pre-k;
            if(ans.containsKey(r)){
                c+=ans.get(r);
            }
            ans.put(pre,ans.getOrDefault(pre,0)+1);
        }
        return c;
    }
}