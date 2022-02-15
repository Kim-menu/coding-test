class Solution {
    public String solution(String s) {
        String[] integers = s.split("\\s");
        int minValue = Integer.MAX_VALUE;
        int maxValue = Integer.MIN_VALUE;
        int curValue;
        for (String integer : integers) {
            curValue = Integer.parseInt(integer);
            minValue = Math.min(minValue, curValue);
            maxValue = Math.max(maxValue, curValue);
        }
        String answer = "";
        answer += Integer.toString(minValue) + " " + Integer.toString(maxValue);
        return answer;
    }
}