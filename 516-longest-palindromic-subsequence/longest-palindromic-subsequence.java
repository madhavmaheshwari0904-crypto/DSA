class Solution {
    public int solve(int i,int j,String s,int[][]dp){
        if(j<i)return 0;
        if(dp[i][j]!=-1)return dp[i][j];
        if(s.charAt(i)==s.charAt(j)){
            if(i==j)return dp[i][j]=1+solve(i+1,j-1,s,dp);
            else  return dp[i][j]=2+solve(i+1,j-1,s,dp);
        }
        return dp[i][j]=Math.max(solve(i+1,j,s,dp),solve(i,j-1,s,dp));
    }
    public int longestPalindromeSubseq(String s) {
      int i=0;
      int j=s.length()-1;
      int [][]dp=new int[s.length()][s.length()];
      for(int[]r:dp)Arrays.fill(r,-1);
      return solve(i,j,s,dp); 
    }
}