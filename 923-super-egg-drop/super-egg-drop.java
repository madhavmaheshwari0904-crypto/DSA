class Solution {
    public int solve(int k,int n,int[][]dp){
        if(n==0 || n==1)return n;
        if(k==1)return n;
        if(dp[k][n]!=-1)return dp[k][n];
        int low=1,high=n,ans=n;//low must be initialize with 1
        while(low<=high){
            int mid=low+(high-low)/2;
            int broken=solve(k-1,mid-1,dp);
            int not_broken=solve(k,n-mid,dp);
            if(broken<not_broken)low=mid+1;
            else{
                high=mid-1;
            }
            ans=Math.min(ans,1+Math.max(broken,not_broken));
        }
        return dp[k][n]=ans;
    }
    public int superEggDrop(int k, int n) {
      int[][]dp=new int[k+1][n+1];
      for(int[]row:dp){
        Arrays.fill(row,-1);
      }
      return solve(k,n,dp);  
    }
}