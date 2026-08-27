class Solution {
    public int maxProfit(int[] prices) {
        int b1=Integer.MAX_VALUE;
        int s1=0;
        int b2=Integer.MAX_VALUE;
        int s2=0;
        for(int i:prices){
            b1=Math.min(b1,i);
            s1=Math.max(s1,i-b1);
            b2=Math.min(b2,i-s1);
            s2=Math.max(s2,i-b2);
        }
        return s2;
    }
}