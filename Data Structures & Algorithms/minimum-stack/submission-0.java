class MinStack {    
    Stack<Integer> min;
    Stack<Integer> stack;
    
    public MinStack() {
        stack = new Stack<>();
        min = new Stack<>();
    }
    
    public void push(int val) {
        if(min.size() < 1 || val < min.peek()) {
            min.push(val);
        } else {
            min.push(min.peek());
        }
        stack.push(val);
    }
    
    public void pop() {
        stack.pop();
        min.pop();
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return min.peek();
    }
}
