import java.util.*;
class Solution {
    public long solution(long n) {
        String[] s = String.valueOf(n).split("");
        StringBuilder sb = new StringBuilder();
        Arrays.sort(s);
        for (int i = 0; i < s.length; i++){
            sb.append(s[i]);     
        }
        return Long.valueOf(sb.reverse().toString());
    }
}