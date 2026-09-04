class Solution {
    public int candy(int[] ratings) {
        int n=ratings.length;
        int ans=0;
        int[]can=new int[n];
        Arrays.fill(can,1);
        for(int i=1;i<n;i++){
            if(ratings[i-1]<ratings[i])can[i]=can[i-1]+1;
        }
        for(int i=n-1;i>0;i--){
            if(ratings[i-1]>ratings[i])can[i-1]=Math.max(can[i]+1,can[i-1]);
            ans+=can[i-1];
        }
        return ans+can[n-1];
    }
}