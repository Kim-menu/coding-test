class Solution {
    public int solution(int n) {
        int answer = 0;
        for (int k = 1; k <= n; k += 2) {
            if (n % k == 0)
                answer++;
        }
        return answer;
    }
}