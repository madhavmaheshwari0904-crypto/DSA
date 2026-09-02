class Solution {
    public int solve(int i,String s,int n,int[]dp){
        if(i==n || ispal(s,i,n-1))return 0;
        if(dp[i]!=-1)return dp[i];
        int mimi=Integer.MAX_VALUE;
        for(int j=i;j<n;j++){
            if(ispal(s,i,j)){
                int cost=1+solve(j+1,s,n,dp);
                mimi=Math.min(mimi,cost);
            }
        }
        return dp[i]=mimi;
    }
    public int minCut(String s) {
        int n=s.length();
        int[]dp=new int[n];
        Arrays.fill(dp,-1);
        return solve(0,s,n,dp);
    }
    public boolean ispal(String s,int i,int j){
        while(i<j){
            if(s.charAt(i)!=s.charAt(j))return false;
            i++;
            j--;
        }
        return true;
    }
}