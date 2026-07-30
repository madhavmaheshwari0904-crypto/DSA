/*class pair{
    int first;
    int second;
    pair(int first,int second){
        this.first=first;
        this.second=second;
    }
}
class tuple{
    int first;
    int second;
    int third;
    tuple(int first ,int second,int third){
        this.first=first;
        this.second=second;
        this.third=third;
    }
}
class Solution {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        ArrayList<ArrayList<Pair>> list=new ArrayList<>();
        for(int i=0;i<n;i++){
            list.add(new ArrayList<>());
        }
        int m=flights.length;
        for(int i=0;i<m;i++){
            list.get(flights[i][0]).add(new pair(flights[i][1],flights[i][2]));
        }
        Queue<tuple>q=new LinkedList<>();
        q.add(new tuple(0,src,0));
        int[] dis =new int[n];
        for(int i=0;i<n;i++){
            dis[i]=(int)1e9;
        }
        dis[src]=0;
        while(!q.isEmpty()){
            tuple t=q.poll();
            int stop=t.first;
            int node=t.second;
            int cost=t.third;
            if(stop>k)continue;
            for(pair i:list.get(node)){
                int u=i.first;
                int v=i.second;
                if(cost+v<dis[u] && stop<=k){
                    dis[u]=cost+v;
                    q.offer(new tuple(stop+1,u,v+cost));
                }
            }
        }
        if(dis[dst]==(int)1e9)return -1;
        return dis[dst];
    }
}*/
class Pair {
    int node;
    int weight;

    Pair(int node, int weight) {
        this.node = node;
        this.weight = weight;
    }
}

class Tuple {
    int stops;
    int node;
    int cost;

    Tuple(int stops, int node, int cost) {
        this.stops = stops;
        this.node = node;
        this.cost = cost;
    }
}

class Solution {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        // 1. Build Adjacency List
        ArrayList<ArrayList<Pair>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adj.add(new ArrayList<>());
        }

        for (int[] flight : flights) {
            adj.get(flight[0]).add(new Pair(flight[1], flight[2]));
        }

        // 2. Queue stores {stops, node, total_cost}
        Queue<Tuple> q = new LinkedList<>();
        q.add(new Tuple(0, src, 0));

        int[] dis = new int[n];
        for (int i = 0; i < n; i++) {
            dis[i] = (int) 1e9;
        }
        dis[src] = 0;

        // 3. BFS traversal level-by-level based on stops
        while (!q.isEmpty()) {
            Tuple t = q.poll();
            int stops = t.stops;
            int node = t.node;
            int cost = t.cost;

            // If stops exceed k, do not expand further neighbors
            if (stops > k) continue;

            for (Pair neighbor : adj.get(node)) {
                int adjNode = neighbor.node;
                int edW = neighbor.weight;

                // Relax edge if a cheaper cost is found within 'k' stops
                if (cost + edW < dis[adjNode] && stops <= k) {
                    dis[adjNode] = cost + edW;
                    q.offer(new Tuple(stops + 1, adjNode, cost + edW));
                }
            }
        }

        return dis[dst] == (int) 1e9 ? -1 : dis[dst];
    }
}