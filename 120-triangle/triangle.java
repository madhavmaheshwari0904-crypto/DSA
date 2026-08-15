class Solution {
    /*public int solve(int[][]dp,int n,int i,int j,List<List<Integer>> triangle){
        if(i==n-1)return triangle.get(n - 1).get(j);
        if(dp[i][j]!=-1)return dp[i][j];
        int d=triangle.get(i).get(j)+solve(dp,n,i+1,j,triangle);
        int dg=triangle.get(i).get(j)+solve(dp,n,i+1,j+1,triangle);
        return dp[i][j]=Math.min(d,dg);
    }*/
    public int minimumTotal(List<List<Integer>> triangle) {
        int n=triangle.size();
        for(int i=n-2;i>=0;i--){
            for(int j=0;j<i + 1;j++){
                int minNext = Math.min(triangle.get(i + 1).get(j), triangle.get(i + 1).get(j + 1));
                int updatedVal = triangle.get(i).get(j) + minNext;
                triangle.get(i).set(j, updatedVal);
            }
        }
        return triangle.get(0).get(0);
    }
}