class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int j = 0;
        for(int i = 0; i < numbers.length; i++) {
            int sum = numbers[i] + numbers[numbers.length-j-1];
            if(sum == target) {
                return new int[]{i+1,numbers.length-j};
            } else if(sum > target) {
                j++;
                i--;
            } else {}
        }
        return null;
    }
}
