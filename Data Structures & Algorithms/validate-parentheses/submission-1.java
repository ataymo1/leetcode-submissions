class Solution {
    public boolean isValid(String s) {
        String left = "([{";
        String right = ")]}";

        Stack<Character> stack = new Stack<>();

        for(char c : s.toCharArray()) {
            if(left.contains(""+ c)) {
                stack.push(c);
            } else {
                if(stack.isEmpty()) {
                    return false;
                } 
                if(stack.peek() != left.charAt(right.indexOf(c))) {
                    return false;
                }
                stack.pop();
            }
        }

        return stack.isEmpty();
    }
}
