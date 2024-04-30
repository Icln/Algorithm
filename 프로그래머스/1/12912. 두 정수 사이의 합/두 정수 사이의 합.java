class Solution {
    public long solution(int a, int b) {
        long answer = 0;
        int tmp = 0;
        if (a > b){
            tmp = b;
            b = a;
            a = tmp;
        }
        
        for (int i = a; i <= b; i++){
            answer += i;
        }
        return answer;
    }
}