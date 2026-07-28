class Solution {
    public String smallestPalindrome(String s) {
        int[] fre=new int[26];
        for(char i:s.toCharArray()){
            fre[i-'a']++;
        }
        int n=s.length();
        char[] ans=new char[n];
        int l=0;
        int r=n-1;
        for(int i=0;i<26;i++){
            while(fre[i]>=2){
                ans[l++]=(char)('a'+i);
                ans[r--]=(char)('a'+i);
                fre[i]-=2;
            }
            if(fre[i]==1){
                ans[n/2]=(char)('a'+i);
            }
        }
        return new String(ans);
    }
}