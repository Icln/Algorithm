class Solution {
    public int solution(int n) {
        int num = 0;
        for (int i = 1; i <= n; i++){
            if (n % i == 0){
                num += i;
            }
        }
        return num;
    }
}