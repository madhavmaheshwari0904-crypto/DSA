class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n=s.length();
        int m=0;
        Map<Character,Integer> map=new HashMap<>();
        int l=0;
        for(int r=0;r<n;r++){
            if(!map.containsKey(s.charAt(r)) || map.get(s.charAt(r))<l){
                map.put(s.charAt(r),r);
                m=Math.max(m,r-l+1);
            }
            else{
                l=map.get(s.charAt(r))+1;
                map.put(s.charAt(r),r);
            }
        }
        return m;
    }
}