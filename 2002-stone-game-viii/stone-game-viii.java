class Solution {
    public int stoneGameVIII(int[] stones) {
        int[]pre=stones.clone();
        int n=stones.length;
        for(int i=1;i<stones.length;i++){
            pre[i]+=pre[i-1];
        }
        int ans=pre[n-1];
        for(int i=n-2;i>=1;i--){
            ans=Math.max(ans,pre[i]-ans);
        }
        return ans;
    }
}