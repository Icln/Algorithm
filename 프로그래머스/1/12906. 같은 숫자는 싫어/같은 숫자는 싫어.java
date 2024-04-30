import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        int[] answer = {};
        Stack<Integer> s = new Stack<Integer>();
        for (int i : arr){
            if (s.size() == 0)
                s.push(i);
            else{
                if (s.peek() == i)
                    continue;
                else{
                    s.push(i);
                }
            }
        }
        
        return s.stream().mapToInt(Integer::intValue).toArray();
    }
}