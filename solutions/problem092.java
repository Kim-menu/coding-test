class Solution {
    public int solution(int n) {
        int[] arr = new int[3];
        int mod = 1234567;
        arr[0] = 0;
        arr[1] = 1;
        for(int i = 0; i < n-1; i++) {
            arr[2] = (arr[0] + arr[1]) % mod;
            arr[0] = arr[1];
            arr[1] = arr[2];
        }
        return arr[2];
    }
}