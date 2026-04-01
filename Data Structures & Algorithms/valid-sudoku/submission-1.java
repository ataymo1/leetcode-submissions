class Solution {
    public boolean isValidSudoku(char[][] board) {
        for(int i = 0; i < board.length; i++) {
            HashSet<Character> set = new HashSet<>();
            boolean hasZero = false;
            int count = 0;
            for(int j = 0; j < board[0].length; j++) {
                if(board[i][j] != '.') {
                    count++;
                } else {
                    hasZero = true;
                }
                set.add(board[i][j]);
            }
            if(hasZero) {
                if(count != set.size() - 1) {
                    return false;
                }
            } else {
                if(count != set.size()) {
                    return false;
                }
            }
        }

        for(int i = 0; i < board.length; i++) {
            HashSet<Character> set = new HashSet<>();
            boolean hasZero = false;
            int count = 0;
            for(int j = 0; j < board[0].length; j++) {
                if(board[j][i] != '.') {
                    count++;
                } else {
                    hasZero = true;
                }
                set.add(board[j][i]);
            }
            if(hasZero) {
                if(count != set.size() - 1) {
                    return false;
                }
            } else {
                if(count != set.size()) {
                    return false;
                }
            }
        }
        for(int l = 0; l < 9; l += 3) {
            for(int k = 0; k < 9; k += 3) {
                HashSet<Character> set = new HashSet<>();
                boolean hasZero = false;
                int count = 0;
                for(int i = 0; i < 3; i++) {
                    for(int j = 0; j < 3; j++) {
                        if(board[j+k][i+l] != '.') {
                            count++;
                        } else {
                            hasZero = true;
                        }
                        set.add(board[j+k][i+l]);
                    }
                }
                if(hasZero) {
                    if(count != set.size() - 1) {
                        return false;
                    }
                } else {
                    if(count != set.size()) {
                        return false;
                    }
                }
            }
        }

        return true;
    }

}
