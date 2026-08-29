class Solution {
    public List<Integer> largestDivisibleSubset(int[] arr) {
        int n = arr.length;
        Arrays.sort(arr);
        List<Integer> ans = new ArrayList<>();
        int[]dp=new int[n];
        Arrays.fill(dp,1);
        int[] parent = new int[n];
        int maxi=1;
        int last=0;
        for(int i=0;i<n;i++){
            parent[i]=i;
            for(int prev=0;prev<i;prev++){
                if(arr[i]%arr[prev]==0 && 1+dp[prev]>dp[i]){
                    dp[i]=1+dp[prev];
                    parent[i]=prev;
                }
            }
            if(dp[i]>maxi){
                maxi=dp[i];
                last=i;
            }
        }
        int i = last;
        while(parent[i] != i) {
            ans.add(arr[i]); 
            i = parent[i]; 
        }
        ans.add(arr[i]);
        return ans;
    }
}