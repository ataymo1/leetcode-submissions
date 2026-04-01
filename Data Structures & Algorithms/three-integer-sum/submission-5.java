class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> sol = new ArrayList<>();
        HashSet<Integer> set = new HashSet<>();

        Arrays.sort(nums); 
        for (int i = 0; i < nums.length; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            HashMap<Integer, Integer> map = new HashMap<>();
            if (!set.contains(nums[i])) {
                int target = -nums[i]; 
                for (int j = i + 1; j < nums.length; j++) {
                    if (map.containsKey(nums[j])) {
                        set.add(nums[i]);
                        sol.add(new ArrayList<>(Arrays.asList(nums[i], map.get(nums[j]), nums[j])));
                        while (j + 1 < nums.length && nums[j] == nums[j + 1]) j++;
                    } else {
                        map.put(target - nums[j], nums[j]);
                    }
                }
            }
        }
        return sol;
    }
}
