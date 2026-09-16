class Solution {
    public int minDays(int[] bloomDay, int m, int k) {
        if(m*k>bloomDay.length)return -1;
        int low=Integer.MAX_VALUE,high=Integer.MIN_VALUE;
        for(int i: bloomDay){
            low=Math.min(low,i);
            high=Math.max(high,i);
        }
        int ans=-1;
        while(low<=high){
            int mid=(low+high)/2;
            int b=0,c=0;
            for(int i:bloomDay){
                if(i<=mid){
                    c+=1;
                    if(c==k){
                        b+=1;
                        c=0;
                    }
                }
                else c=0;
            }
            if(b>=m){
                ans=mid;
                high=mid-1;
            }
            else low=mid+1;
        }
        return ans;
    }
}