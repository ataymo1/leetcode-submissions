class Solution {
    public boolean isAnagram(String s, String t) {

        ArrayList<Character> tree1 = new ArrayList<>();
        ArrayList<Character> tree2 = new ArrayList<>();

        if(s.length() == t.length()) {
            for(int i = 0; i < s.length(); i++) {
                tree1.add(s.charAt(i));
                tree2.add(t.charAt(i));
            }

            for(char l : tree2) {
                if(!tree1.contains(l)) {
                    return false;
                }
                tree1.remove(Character.valueOf(l));
            }
            return true;
            

       
        }
        return false;
    }
}
