class pair{
    String frist;
    int len;
    pair(String frist,int len){
        this.frist=frist;
        this.len=len;
    }
}
class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        Queue<pair> ans=new LinkedList<>();
        ans.add(new pair(beginWord,1));
        Set<String> st=new HashSet<>();
        int n=wordList.size();
        for(int i=0;i<n;i++){
            st.add(wordList.get(i));
        }
        st.remove( beginWord);
        while(!ans.isEmpty()){
            String word=ans.peek().frist;
            int step=ans.peek().len;
            ans.remove();
            if(word.equals(endWord)==true)return step;
            for(int i=0;i<word.length();i++){
                for(char j='a';j<='z';j++){
                    char[] arr=word.toCharArray();
                    arr[i]=j;
                    String replace=new String(arr);
                    if(st.contains(replace)==true){
                        st.remove(replace);
                        ans.add(new pair(replace,step+1));
                    }
                }
            }
        }
        return 0;
    }
}