class Solution {
    public String solution(int a, int b) {
        int[] month = {0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        
        String[] answer = {"THU","FRI","SAT","SUN","MON","TUE","WED"};
        
        int tmp = 0;
        for (int i = 1; i < a; i++){
            tmp += month[i];
        }
        tmp += b;
        
        return answer[tmp%7];
    }
}