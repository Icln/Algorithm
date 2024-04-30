import java.util.*;
class Solution {
    public double solution(int[] arr) {
        double num = Arrays.stream(arr).sum();
        double answer = num / arr.length;
        return answer;
    }
}