class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> map = new HashMap<>();
        
        for (String s : strs) {
            char[] c = new char[26];
            for (int i = 0; i < s.length(); i++) {
                c[s.charAt(i) - 'a']++;
            }
            String key = new String(c);
            if (!map.containsKey(key)) {
                map.put(key, new ArrayList<>());
            }
            map.get(key).add(s);
        }
        
        return new ArrayList<>(map.values());
    }
}
