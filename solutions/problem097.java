class Solution {
    public int solution(int n) {
        int originOnesCount = getOnesCount(n++);
        while (originOnesCount != getOnesCount(n))
            n++;
        return n;
    }
    public int getOnesCount(int n) {
        int onesCount = 0;
        while(n > 0) {
            if (n % 2 == 1)
                onesCount++;
            n /= 2;
        }
        return onesCount;
    }
}