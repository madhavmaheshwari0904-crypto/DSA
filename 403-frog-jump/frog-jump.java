class Solution {
    public boolean canCross(int[] stones) {
        Map<Integer,HashSet<Integer>> map=new HashMap<>();
        for(int i=0;i<stones.length;i++){
            map.put(stones[i],new HashSet<>());
        }
        map.get(stones[0]).add(1);
        for (int i = 0; i < stones.length; i++) {
            int currentStone = stones[i];
            Set<Integer> jumps = map.get(currentStone);
            for (int jump : jumps) {
                int nextPos = currentStone + jump;
                if (nextPos == stones[stones.length - 1]) {
                    return true;
                }
                if (map.containsKey(nextPos)) {
                    if (jump - 1 > 0) {
                        map.get(nextPos).add(jump - 1);
                    }
                    map.get(nextPos).add(jump);
                    map.get(nextPos).add(jump + 1);
                }
            }
        }
        return false;
    }
}