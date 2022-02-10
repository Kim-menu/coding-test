class Solution {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        int m = arr1.length;
        int k = arr1[0].length;
        int n = arr2[0].length;
        int[][] answer = new int[m][n];
        for(int row = 0; row < m; row++) {
            for(int col = 0; col < n; col++) {
                for(int mid = 0; mid < k; mid++)
                    answer[row][col] += arr1[row][mid] * arr2[mid][col];
            }
        }
        return answer;
    }
}