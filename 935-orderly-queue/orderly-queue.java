class Solution {
    public String orderlyQueue(String s, int k) {
        if(k>1){
            char tempArray[] = s.toCharArray();
            Arrays.sort(tempArray);
            return new String(tempArray);
        }
        String ans  = s+s;
        int i=0,j=1;
        int n=s.length(); 
            while(i<n && j<n){
                int shift=0;
                while(shift<n && ans.charAt(i+shift)==ans.charAt(j+shift))shift+=1;
                if(shift==n)break;
                if(ans.charAt(i+shift)>ans.charAt(j+shift)){
                    i=i+shift+1;
                    if(i<=j)i=j+1;
                }else{
                    j=j+shift+1;
                    if(j<=i)j=i+1;
                }
            }
            int start=Math.min(i,j);
        return ans.substring(start,start+n);
    }
}