class Solution {
    public int maxScore(int[] cardPoints, int k) {
        int n=cardPoints.length;
        int s=0;
        for(int i=0;i<k;i++){
            s+=cardPoints[i];
        }
        int m=s;
        for(int i=1;i<k+1;i++){
            s+=cardPoints[n-i]-cardPoints[k-i];
            if(s>m)m=s;
        }
        return m;
    }
}