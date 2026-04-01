class Solution {
    public int longestConsecutive(int[] nums) {
        TreeSet<Integer> set = new TreeSet<>();
        for(int num : nums) {
            set.add((Integer)num);
        }
        HashMap<Integer, Integer> map = new HashMap<>();

        for(int num : set) {
            if(map.containsKey(num)) {
                map.put(num+1, map.get(num)+1);
            } else {
                map.put(num+1, 1);
            }
        }

        int max = 0;
        for(Map.Entry<Integer, Integer> entry : map.entrySet()) {
            if(entry.getValue() > max) {
                max = entry.getValue();
            }
        }

        return max;
    }
}
