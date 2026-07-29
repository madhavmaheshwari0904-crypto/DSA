class Solution {
    public boolean makesquare(int[] matchsticks) {
        if(matchsticks==null || matchsticks.length<4)return false;
        int side=0;
        for(int i:matchsticks){
            side+=i;
        }
        if(side%4!=0)return false;
        Arrays.sort(matchsticks);
        reverse(matchsticks);
        int[] ans=new int[4];
       return dfs(matchsticks,ans,0,side/4); 
    }
    public boolean dfs(int[] box,int[] ans,int idx,int t){
        if(idx==box.length)return true;
        for(int i=0;i<4;i++){
            if((ans[i]+box[idx]>t)||(i>0 && ans[i]==ans[i-1]))continue;
            ans[i]+=box[idx];
            if(dfs(box,ans,idx+1,t))return true;
            ans[i]-=box[idx];
        }
        return false;
    }
    private void reverse(int[] arr) {
        int i = 0, j = arr.length - 1;
        while (i < j) {
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
            i++;
            j--;
        }
    }
}