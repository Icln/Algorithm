class Solution {
    public int solution(String t, String p) {
        int len = p.length();
        long pNum = Long.valueOf(p);
        int answer = 0;
        for (int i = 0; i <= t.length() - p.length(); i++){
            long tmp = Long.valueOf(t.substring(i, i + p.length()));
            if (tmp <= pNum)
                answer++;
        }
        return answer;
    }
}