class Solution {

    public String encode(List<String> strs) {
        String code = "";
        if(strs.size() == 0) {
            return "#55";
        }
        for(int i = 0; i < strs.size(); i++) {
            code += strs.get(i) + "#5";
        }
        return code;
    }

    public List<String> decode(String str) {
        ArrayList<String> list = new ArrayList<>();
        String[] strs = str.split("#5");
        if(str.equals("#55")) {
            return list;
        } else if (str.equals("#5")) {
            list.add("");
            return list;
        }
        for(String s : strs) {
            list.add(s);
        }
        return list;
    }
}
