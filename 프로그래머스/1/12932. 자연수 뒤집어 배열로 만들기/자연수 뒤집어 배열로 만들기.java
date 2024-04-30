class Solution {
    public int[] solution(long n) {
        String a = n + "";
        int[] answer = new int[a.length()];

        int cnt=0;

        while(n > 0) {
            answer[cnt]=(int)(n%10);
            n/=10;
            System.out.println(n);
            cnt++;
        }
    
        return answer;
    }
}