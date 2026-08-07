class Disjoint{
    List<Integer> rank=new ArrayList<>();
    List<Integer> parent=new ArrayList<>();
    public Disjoint(int n){
        for(int i=0;i<n;i++){
            rank.add(0);
            parent.add(i);
        }
    }
    public int ultimateparent(int node){
        if(node==parent.get(node))return node;
        int ulp=ultimateparent(parent.get(node));
        parent.set(node,ulp);
        return parent.get(node);
    }
    public void unionRank(int u,int v){
        int ulp=ultimateparent(u);
        int vlp=ultimateparent(v);
        if(ulp==vlp)return;
        if(rank.get(ulp)>rank.get(vlp)){
            parent.set(vlp,ulp);
        }
        else if(rank.get(ulp)<rank.get(vlp)){
            parent.set(ulp,vlp);
        }
        else{
            parent.set(vlp,ulp);
            int r=rank.get(ulp);
            rank.set(ulp,r+1);
        }
    }
}
class Solution {
    public int makeConnected(int n, int[][] connections) {
        Disjoint set=new Disjoint(n);
        int e=0;
        int m=connections.length;
        for(int i=0;i<m;i++){
            int u=connections[i][0];
            int v=connections[i][1];
            if(set.ultimateparent(u)==set.ultimateparent(v))e++;
            else set.unionRank(u,v);
        }
        int c=0;
        for( int i=0;i<n;i++){
            if(set.parent.get(i)==i)c++;
        }
        int ans=c-1;
        if(e>=ans)return ans;
        return -1;
    }
}