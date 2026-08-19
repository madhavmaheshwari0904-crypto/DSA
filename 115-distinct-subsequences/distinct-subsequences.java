class Solution {
    /*public int solve(String s, String t,int i,int j){
        if(i<0 || j<0 || i<j)return 0;
        if(s.charAt(i)==t.charAt(j)){
            if(j==0)return 1+solve(s,t,i-1,j);
            else return solve(s,t,i-1,j-1)+solve(s,t,i-1,j);
        }
        return solve(s,t,i-1,j);
    }*/
    //TLE TC(2^n);
    public int solve(String s, String t,int i,int j,int[][]dp){
        if(j<0)return 1;
        if(i<0 || j<0 ||i<j)return 0;
        if (dp[i][j] != -1) return dp[i][j];
        if(s.charAt(i)==t.charAt(j)){
            dp[i][j]=solve(s,t,i-1,j-1,dp)+solve(s,t,i-1,j,dp);
        }
        else{
            dp[i][j]=solve(s,t,i-1,j,dp);
        }
        return dp[i][j];
    }
    public int numDistinct(String s, String t) {
        int n=s.length();
        int m=t.length();
        int[][]dp=new int[n][m];
        for(int[]row:dp){
            Arrays.fill(row,-1);
        }
        return solve(s,t,n-1,m-1,dp);
    }
}