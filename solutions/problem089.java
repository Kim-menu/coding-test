class Solution {
    public int solution(int[] arr) {
        int answer = 1;
        for(int cur : arr) {
            answer = getLcm(Math.max(answer, cur), Math.min(answer, cur));
        }
        return answer;
    }

    public int getGcd(int big, int small) {
        int quotient = big / small;
        int remainder = big % small;
        if (remainder > 0)
            return getGcd(small, remainder);
        else
            return small;
    }

    public int getLcm(int big, int small) {
        return big * small / getGcd(big, small);
    }
}