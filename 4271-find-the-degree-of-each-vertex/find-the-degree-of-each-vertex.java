class Solution {
    public int[] findDegrees(int[][] matrix) {
        int m=matrix.length;//number of rows
        int n=matrix[0].length;//number of colums
        int[] ans=new int[m];//ans array of size to number of rows
        for(int i=0;i<m;i++){
            int s=0;
            for (int j=0;j<n;j++)
                s+=matrix[i][j];
            ans[i]=s;
        }
        return ans; 
    }
}