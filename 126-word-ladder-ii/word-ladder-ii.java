class Solution {
    Map<String, Integer> map;
    List<List<String>> ans;
    String beginWord;
    public List<List<String>> findLadders(String beginWord, String endWord, List<String> wordList) {
        /*Set<String>set=new HashSet<String>();
        int l=wordList.size();
        for(int i=0;i<l;i++)set.add(wordList.get(i));
        Queue<ArrayList<String>>q=new LinkedList<>();
        ArrayList<String>list=new ArrayList<>();
        list.add(beginWord);
        q.add(list);
        ArrayList<String>level=new ArrayList<>();
        level.add(beginWord);
        int n=0;
        List<List<String>>ans=new ArrayList<>();
        while(!q.isEmpty()){
            ArrayList<String> vec=q.peek();
            q.remove();
            if(vec.size()>n){
                n++;
                for(String i:level)set.remove(i);
            }
            String word=vec.get(vec.size()-1);
            if(word.equals(endWord)){
                if(ans.size()==0)ans.add(vec);
                else if(ans.get(0).size()==vec.size())ans.add(vec);
            }
            for(int i=0;i<word.length();i++){
                for(char j='a';j<='z';j++){
                    char[] arr=word.toCharArray();
                    arr[i]=j;
                    String replace=new String(arr);
                    if(set.contains(replace)==true){
                        vec.add(replace);
                        ArrayList<String>temp=new ArrayList<>(vec);
                        q.add(temp);
                        level.add(replace);
                        vec.remove(vec.size()-1);
                    }
                }
            }
        }
        return ans;*/
        Set<String> set = new HashSet<>(wordList);
        Deque<String> q = new ArrayDeque<>();
        this.beginWord = beginWord;
        q.offer(beginWord);
        set.remove(beginWord);
        map = new HashMap<>();
        map.put(beginWord, 0);
         while(!q.isEmpty()){
            String word = q.poll();
            int step = map.get(word);
            if(word.equals(endWord))
                break;
            char[] arr = word.toCharArray();
            for(int i = 0; i < word.length(); i++){
                char original = arr[i];
                for(char ch = 'a'; ch <= 'z'; ch++){
                    arr[i] = ch;
                    String newWord = new String(arr);
                    if(set.contains(newWord)){
                        set.remove(newWord);
                        q.offer(newWord);
                        map.put(newWord, step + 1);
                    }
                }
                arr[i] = original;
            }
        }
        ans=new ArrayList<>();
        if(map.containsKey(endWord)){

            List<String> seq = new ArrayList<>();
            seq.add(endWord);

            dfs(endWord, seq);
        }
        return ans;
    }
    public void dfs(String word,List<String>seq){
        if(word.equals(beginWord)){

            List<String> temp = new ArrayList<>(seq);

            Collections.reverse(temp);

            ans.add(temp);

            return;
        }
        int steps = map.get(word);

        char[] arr = word.toCharArray();

        for(int i = 0; i < word.length(); i++){

            char original = arr[i];

            for(char ch = 'a'; ch <= 'z'; ch++){

                arr[i] = ch;

                String newWord = new String(arr);

                if(map.containsKey(newWord) &&
                   map.get(newWord) == steps - 1){

                    seq.add(newWord);

                    dfs(newWord, seq);

                    seq.remove(seq.size() - 1);
                }
            }

            arr[i] = original;
        }
    }
}