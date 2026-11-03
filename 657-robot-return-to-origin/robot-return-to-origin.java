class Solution {
    public boolean judgeCircle(String moves) {
        int h=0;
        int v=0;
        for(char i: moves.toCharArray()){
            if(i=='L') v++;
            else if(i == 'R') v--;
            else if(i == 'U') h++;
            else if(i== 'D') h--;
        }
        return h==0 && v==0;
    }
}