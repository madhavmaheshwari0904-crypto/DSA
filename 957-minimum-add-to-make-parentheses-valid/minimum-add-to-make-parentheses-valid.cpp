class Solution {
public:
    int minAddToMakeValid(string s) {
        int open_needed = 0;  // Counts unmatched ')'
        int close_needed = 0; // Counts unmatched '('

        for (char ch : s) {
            if (ch == '(') {
                close_needed++;
            } else { // ch == ')'
                if (close_needed > 0) {
                    close_needed--; // Match with an existing '('
                } else {
                    open_needed++;  // No '(' available to match this ')'
                }
            }
        }

        // Total additions needed = unmatched '(' + unmatched ')'
        return open_needed + close_needed;
    }
};
