class Solution {
    public List<String> fullJustify(String[] word, int maxWidth) {
        List<String> ans = new ArrayList<>();
        int i = 0;
        while (i < word.length) {
            int sum = 0;
            sum = sum + word[i].length();
            int j = i + 1;
            while (j < word.length) {
                if (sum + 1 + word[j].length() > maxWidth)
                    break;
                sum += 1 + word[j].length();
                j++;
            }
            StringBuilder line = new StringBuilder();
            int diff = j - i - 1;

            if (j == word.length || diff == 0) {
                line.append(word[i]); 
                for (int k = i + 1; k < j; k++) {
                    line.append(" ");
                    line.append(word[k]);
                }
                for (int k = line.length(); k < maxWidth; k++) {
                    line.append(" ");
                }
            } else {
                line.append(word[i]); 
                int spaces = (maxWidth - sum) / diff; 
                int extra = (maxWidth - sum) % diff; 
                for (int k = i + 1; k < j; k++) { 
                    for (int s = spaces; s > 0; s--) {
                        line.append(" ");
                    }
                    if (extra > 0) {
                        line.append(" ");
                        extra--;
                    }
                    line.append(" ");
                    line.append(word[k]);
                }
            }
            ans.add(line.toString());
            i = j; 
        }
        return ans;
    }
}