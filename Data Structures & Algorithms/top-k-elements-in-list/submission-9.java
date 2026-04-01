class Solution {
    public int[] topKFrequent(int[] nums, int k) {
       HashMap<Integer, ArrayList<Integer>> map = new HashMap<>();
       int[] sol = new int[k];
       for(int num : nums) {
        if(map.containsKey(num)) {
            map.get(num).add(num);
        } else {
            ArrayList<Integer> list = new ArrayList<>();
            list.add(num);
            map.put(num, list);
        }
       } 
       
       for(int i = 0; i < k; i++) {
        int max = 0;
        int val = 0;
        for(Map.Entry<Integer, ArrayList<Integer>> entry : map.entrySet()) {
            if(entry.getValue().size() > max) {
                max = entry.getValue().size();
                val = entry.getKey();
            } 
        }
        map.remove(val);
        sol[i] = val;
       }
       return sol;
    }
}
