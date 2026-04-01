class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = [];
        for t in tokens:
            try:
                num = int(t);
                s.append(num);
            except ValueError:
                n1 = s.pop();
                n2 = s.pop();
                match t:
                    case "+":
                        s.append(n2+n1);
                    case "-":
                        s.append(n2-n1);
                    case "*":
                        s.append(n2*n1);
                    case "/":
                        s.append(int(n2/n1));
        return s.pop();

        return;
        