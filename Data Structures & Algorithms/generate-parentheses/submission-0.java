class Solution {
    List<String> list;
    Stack<String> stack;

    public List<String> generateParenthesis(int n) {
        
        list = new ArrayList<>();
        stack = new Stack();
        backtrack(0, 0, n);
        return list;
        
    }
    public void backtrack(int ln, int rn, int n) {
        if(ln == n && rn == n) {
            list.add(String.join("", stack));
            return;
        }

        if(ln < n) {
            stack.push("(");
            backtrack(ln + 1, rn, n);
            stack.pop();
        }

        if(rn < ln) {
            stack.push(")");
            backtrack(ln, rn + 1, n);
            stack.pop();
        }
    }

    
}
