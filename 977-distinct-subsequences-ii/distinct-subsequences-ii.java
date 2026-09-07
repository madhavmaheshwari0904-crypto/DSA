class Solution {
    public int distinctSubseqII(String s) {
    int mod = 1_000_000_007;
    int ans = 0;
    int[] dp = new int[26];
    
    for (int i = 0; i < s.length(); i++) {
        int c = s.charAt(i) - 'a';
        int add = (ans + 1 - dp[c] + mod) % mod;
        ans = (ans + add) % mod;
        dp[c] = (dp[c] + add) % mod;
    }
    return ans;
    }
}