class Solution {
    public int climbStairs(int n) {
        /*int a=1;
        int b=1;
        int c=0;
        for(int i=0;i<n;i++){
            c=a+b;
            a=b;
            b=c;
        }
        return a;*/
        int[] dp=new int[n+1];
        Arrays.fill(dp,-1);
        dp[0]=0;
        dp[1]=1;
        int ans=clime(dp,n);
        return ans;
    }
    public static int clime(int[]dp,int n){
        if(n<=1)return 1;
        if(dp[n]!=-1)return dp[n];
        return dp[n]=clime(dp,n-1)+clime(dp,n-2);
    }
}