import java.util.*;
class Solution {
    static HashSet<String> nums = new HashSet<>();
    static int answer;
    static void dfs(String s, int cur, int next, int target, int[] numbers){
        if(next == numbers.length){
            if(!nums.contains(s) && cur == target){
                nums.add(s);
                answer++;
            }
            return;
        }
        dfs(s + "-" + numbers[next], cur - numbers[next], next + 1, target, numbers);
        dfs(s + "+" + numbers[next], cur + numbers[next], next + 1, target, numbers);
    }
    public int solution(int[] numbers, int target) {
        dfs("-" + numbers[0], numbers[0], 1, target, numbers);
        dfs("+" + numbers[0], -numbers[0], 1, target, numbers);
        return answer;
    }
}