import java.util.Arrays;

class Solution {
    public int solution(int[] A, int[] B) {
        int answer = 0;
        Arrays.sort(A);
        reverseSort(B);
        for (int i = 0; i < A.length; i++)
            answer += A[i]*B[i];
        return answer;
    }

    public void reverseSort(int[] arr) {
        int temp;
        Arrays.sort(arr);
        for (int i = 0; i < arr.length / 2; i++) {
            temp = arr[i];
            arr[i] = arr[arr.length - 1 - i];
            arr[arr.length - 1 - i] = temp;
        }
        return;
    }
}