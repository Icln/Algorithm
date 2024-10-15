class Solution {
    static int l, r, answer;
    static boolean check(int mid, int k, int[] stones){
        int cnt = 0;
        for (int stone : stones) {
            if (stone - mid < 0) cnt++;
            else cnt = 0;
            if (cnt == k) return false;
        }
        return true;
    }
    
    public int solution(int[] stones, int k) {
        l = 1;
        r = 200000000;
        while(l <= r){
            int mid = (l + r) / 2;
            if(check(mid, k, stones)){
                l = mid + 1;
                answer = Math.max(answer, mid);
            }
            else
                r = mid - 1;
        }
        return answer;
    }
}
