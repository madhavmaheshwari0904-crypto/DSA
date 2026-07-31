class Solution {
    public int minimumPushes(String word) {
      int[] fre =new int[26];
      for(char i:word.toCharArray()){
        fre[i-'a']++;
      }
      Arrays.sort(fre);
      int ans=0;
      int idx=0;
      for(int i=25;i>=0 &&fre[i]>0;i--){
         ans+=fre[i]*(idx/8+1);
         idx++;
      }
      return ans;
    }
}