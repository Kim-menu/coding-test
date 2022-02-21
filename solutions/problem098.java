import java.util.Stack;

class Solution {
    boolean solution(String s) {
        boolean answer = true;
        Stack<Integer> parentheses = new Stack<>();
        for (char c : s.toCharArray()) {
            if (c == '(')
                parentheses.push(1);
            else {
                try {
                    parentheses.pop();
                } catch (Exception e) {
                    answer = false;
                    break;
                }
            }
        }
        if (!parentheses.empty())
            answer = false;
        return answer;
    }
}