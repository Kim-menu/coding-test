class Solution {
    public String solution(String s) {
        String answer = "";
        boolean upperNow = true;
        for(int i = 0; i < s.length(); i++) {
            char curChar = s.charAt(i);
            if (upperNow && curChar != ' ') {
                answer += getUpperCase(curChar);
                upperNow = false;
            }
            else {
                answer += getLowerCase(curChar);
                if (curChar == ' ')
                    upperNow = true;
            }
        }
        return answer;
    }

    public char getLowerCase(char alphabet) {
        int result = (int) alphabet;
        if (alphabet >= 'A' && alphabet <= 'Z')
            result += ('a' - 'A');
        return (char) result;
    }

    public char getUpperCase(char alphabet) {
        int result = (int) alphabet;
        if (alphabet >= 'a' && alphabet <= 'z')
            result -= ('a' - 'A');
        return (char) result;
    }
}