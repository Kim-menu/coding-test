import java.util.Arrays;

class Solution {
    int solution(int[][] land) {
        int[][] dp = new int[land.length][4];
        dp[0] = land[0];
        for (int row = 1; row < land.length; row++) {
            for (int col = 0; col < 4; col++)
                calcDp(row, col, dp, land);
        }
        Arrays.sort(dp[land.length-1]);
        return dp[land.length-1][3];
    }
    void calcDp(int row, int col, int[][] dp, int[][] land) {
        int maxDp = 0;
        for(int curCol = 0; curCol < 4; curCol++) {
            if (curCol == col)
                continue;
            maxDp = Math.max(maxDp, dp[row-1][curCol]);
        }
        dp[row][col] = maxDp + land[row][col];
        return;
    }
}