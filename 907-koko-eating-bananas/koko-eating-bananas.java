class Solution {
    public int solve(int start,int end,int[]piles,int hours,int ans){
        int h=hours;
        if(start>end)return ans;
        int mid=start+(end-start)/2;
        for(int i=0;i<piles.length;i++){
            int curr=piles[i];
            if(h==0){
                return solve(mid+1,end,piles,hours,ans);
            }
            h-=(curr+mid-1)/mid;
        }
        if(h>=0){
            ans=Math.min(ans,mid);
            return solve(start,mid-1,piles,hours,ans);
        }
        else return solve(mid+1,end,piles,hours,ans);
    }
    public int minEatingSpeed(int[] piles, int h) {
        int m=0;
        for(int i=0;i<piles.length;i++){
            m=Math.max(m,piles[i]);
        }
        return solve(1,m,piles,h,m);
    }
}