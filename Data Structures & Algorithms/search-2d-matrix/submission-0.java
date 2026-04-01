class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int left = 0;
        int right = matrix[0].length-1;
        int pos = -1;
        int l = 0;
        int r = matrix.length-1;

        while(l <= r) {
            int middle = (l + r) / 2;
            if(matrix[middle][0] > target) {
                r = middle - 1;
            } else if(matrix[middle][matrix[middle].length-1] < target) {
                l = middle + 1;
            } else {
                pos = middle;
                break;
            }
        }

        if(pos == -1) {
            return false;
        }

        while(left <= right) {
            int middle = (left + right) / 2;
            if(matrix[pos][middle] == target) {
                return true;
            } else if(target > matrix[pos][middle]) {
                left = middle + 1;
            } else {
                right = middle - 1;
            }
        }
        return false;
    }
}
