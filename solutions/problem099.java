class Solution
{
    public int solution(int [][]board)
    {
        int answer = 0;
        int m = board.length;
        int n = board[0].length;
        int[][] dp = new int[m][n];
        dp[0] = board[0];
        for (int row = 0; row < m; row++) {
            for (int col = 0; col < n; col++) {
                if(board[row][col] == 1) {
                    if (row == 0 || col == 0)
                        dp[row][col] = board[row][col];
                    else {
                        dp[row][col] = Math.min(Math.min(dp[row-1][col], dp[row][col-1]), dp[row-1][col-1]) + 1;
                    }
                    answer = Math.max(dp[row][col], answer);
                }
            }
        }
        return answer*answer;
    }
}