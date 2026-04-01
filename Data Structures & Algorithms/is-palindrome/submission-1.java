class Solution {
    public boolean isPalindrome(String s) {
        s = s.toLowerCase();
        String str = "";
        for(char c : s.toCharArray()) {
            if((c >= 'a' && c <= 'z') || (c>= '0' && c <= '9')) {
                str += c;
            }
        }

        for(int i = 0; i < str.length()/2; i++) {
            if(str.charAt(i) != str.charAt(str.length()-i-1)) {
                return false;
            }
        }
        return true;
    }
}
