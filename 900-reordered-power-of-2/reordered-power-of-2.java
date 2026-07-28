class Solution {
    public boolean reorderedPowerOf2(int n) {
        char[] s=sortedDigits(n);
        for(int i=0;i<30;i++){
            char[]power=sortedDigits(1<<i);
            if(Arrays.equals(s,power))return true;
        }
        return false;
    }
    public char[] sortedDigits(int n){
        char[] ans=String.valueOf(n).toCharArray();
        Arrays.sort(ans);
        return ans;
    }
}